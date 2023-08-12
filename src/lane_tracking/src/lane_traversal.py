import rospy
import cv2
from cv_bridge import CvBridge
import numpy as np
import pickle
import rosbag

from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import CompressedImage, Image

class Listener:
    def __init__(self, cam_topic, output_topic):
        rospy.init_node('lanetracking')

        self.K = np.array([230.93880164921563, 0.0, 400.5, -0.0, 0.0, 230.93880164921563, 400.5, 0.0, 0.0, 0.0, 1.0, 0.0]).reshape(3, 4)

        self.bridge = CvBridge()

        self.state_mt = rospy.Subscriber('/hummingbird/odometry_sensor1/pose', PoseStamped, self.state_cb)
        self.cam_sub = rospy.Subscriber('/hummingbird/camera_hummingbird/image_raw', Image, self.cam_cb)

        self.z = 1

        self.cam_center = 800//2, 800//2

        self.target_color = np.array([[[255, 0, 0]]], np.uint8)
        hsvBlue = cv2.cvtColor(self.target_color, cv2.COLOR_BGR2HSV)
        self.lowerLimit = np.array((hsvBlue[0][0][0] - 10, 100, 100))
        self.upperLimit = np.array((hsvBlue[0][0][0] + 10, 255, 255))

        self.output_pub = rospy.Publisher(output_topic, PoseStamped)

    def state_cb(self, msg: PoseStamped):
        rospy.logerr('Reached Here')
        self.z = msg.pose.position.z - 0.05

    def cam_cb(self, msg: Image):
        
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)

        self.process(cv_img)

    def calculate_closest_indices(self, indices):
        distances = np.square(indices[:, 0] - self.cam_center[1]) + np.square(indices[:, 1] - self.cam_center[0])
        closest_ind = np.argmin(distances)
        delta = 200
        forward, backward = max(0, closest_ind - delta), min(len(distances), closest_ind + delta)
        return forward, backward

    def process(self, img: cv2.Mat):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img_hsv, self.lowerLimit, self.upperLimit)
        indices = np.argwhere(mask)

        if indices.shape[0] == 0:
            cv2.circle(img, center = self.cam_center, radius=5, color=(200, 255, 50), thickness=-1, lineType=cv2.LINE_AA)

            cv2.imshow('Cam Perception', img)
            cv2.waitKey(1)

            return
            
        forward, _ = self.calculate_closest_indices(indices)

        uv = np.array([indices[forward][::-1][0], indices[forward][::-1][1], 1])
        newK = np.ones((3, 3))
        newK[:, :] = self.K[:, :-1]
        newK[:, -1] = self.K[:, -1] + self.K[:, -2] * self.z

        xyz = np.linalg.pinv(newK) @ uv

        pose = PoseStamped()

        pose.header.frame_id = 'hummingbird/camera_hummingbird_optical_link'
        
        pose.pose.position.x = xyz[0]
        pose.pose.position.y = xyz[1]
        pose.pose.position.z = 0

        pose.pose.orientation.w = 0
        pose.pose.orientation.x = 0.707
        pose.pose.orientation.y = -0.707
        pose.pose.orientation.z = 0

        self.output_pub.publish(pose)

        cv2.circle(img, center = self.cam_center, radius=5, color=(200, 255, 50), thickness=-1, lineType=cv2.LINE_AA)
        cv2.circle(img, center = indices[forward][::-1], radius=5, color=(255, 200, 50), thickness=-1, lineType=cv2.LINE_AA)

        cv2.imshow('Cam Perception', img)
        cv2.waitKey(1)

if __name__ == '__main__':
    listener = Listener('/hummingbird/camera_hummingbird/image_raw', '/waypoint_topic')

    rospy.spin()
