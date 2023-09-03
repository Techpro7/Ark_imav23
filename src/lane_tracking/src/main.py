import rospy

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Pose

import numpy as np
import cv2

init_pose = Pose()

class ListenerNode:

    pose = init_pose
    lin_vel = [0, 0, 0]
    
    # Frequency of IMU topic
    dt = 0.001

    def __init__(self, imu_topic: str, out_topic: str):
        rospy.init_node('imu_visualizer')

        self.imu_sub = rospy.Subscriber(imu_topic, Imu, self.imu_callback)
        self.pose_pub = rospy.Publisher(out_topic, Pose)

    def imu_callback(self, msg: Imu):
        angular_velocity = msg.angular_velocity
        orientation = msg.orientation
        lin_acc = msg.linear_acceleration

        # Subtract gravity, I have no idea why its present in the first place
        lin_acc.z = lin_acc.z - 9.8

        self.pose.position.x += self.lin_vel[0] * self.dt + 0.5 * lin_acc.x * self.dt ** 2
        self.pose.position.y += self.lin_vel[1] * self.dt + 0.5 * lin_acc.y * self.dt ** 2
        self.pose.position.y -= self.lin_vel[2] * self.dt + 0.5 * lin_acc.z * self.dt ** 2

        self.lin_vel[0] += lin_acc.x * self.dt
        self.lin_vel[1] += lin_acc.y * self.dt
        self.lin_vel[2] += lin_acc.z * self.dt

        self.pose.orientation = orientation

        self.pose_publish()

    def pose_publish(self):
        msg = self.pose        
        self.pose_pub.publish(msg)

def main():
    node = ListenerNode('/hummingbird/vi_sensor/imu', '/filtered_pose_from_imu')

    try: 
        rospy.spin()
    except Exception as e:
        rospy.logerr(e)

if __name__ == '__main__':
    main() 