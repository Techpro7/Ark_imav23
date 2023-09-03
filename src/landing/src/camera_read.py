#!/usr/bin/env python

import rospy

import pyzbar.pyzbar as zbar
from pyzbar.pyzbar import Decoded, Point

import cv2
import numpy as np
import tf2_geometry_msgs

from sensor_msgs.msg import Image
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import PoseStamped
from cv_bridge import CvBridge, CvBridgeError

def euler_to_quaternion(roll, pitch, yaw):
	qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
	qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
	qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
	qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

	return qx, qy, qz, qw

class camera_hummingbird:

	def __init__(self):
		self.read_camera_parameters()
		
		self.state_mt = rospy.Subscriber('/hummingbird/odometry_sensor1/pose', PoseStamped, self.state_cb)
        
		self.image_sub = rospy.Subscriber("/hummingbird/camera_hummingbird/image_raw", Image, self.callback)
		# self.qr = cv2.QRCodeDetector()
		self.qr = zbar.decode
		self.waypoint_pub = rospy.Publisher("/waypoint_topic", PoseStamped)
		
		self.z = 1

	def state_cb(self, msg: PoseStamped):
		self.z = msg.pose.position.z - 0.05

	def read_camera_parameters(self, filepath = '/home/aryansatpathy/DevStuff/imav/src/landing/params/cam_params.txt'):

		inf = open(filepath, 'r')

		cmtx = []
		dist = []

		#ignore first line
		line = inf.readline()
		for _ in range(3):
				line = inf.readline().split()
				line = [float(en) for en in line]
				cmtx.append(line)

		#ignore line that says "distortion"
		line = inf.readline()
		line = inf.readline().split()
		line = [float(en) for en in line]
		dist.append(line)

		#cmtx = camera matrix, dist = distortion parameters
		self.cmtx, self.dist =  np.array(cmtx), np.array(dist)

	def get_qr_coords(self, points):

		#Selected coordinate points for each corner of QR code.
		qr_edges = np.array([[0,0,0],
												 [0,1,0],
												 [1,1,0],
												 [1,0,0]], dtype = 'float32').reshape((4,1,3))

		#determine the orientation of QR code coordinate system with respect to camera coorindate system.
		ret, rvec, tvec = cv2.solvePnP(qr_edges, points, self.cmtx, self.dist)

		#Define unit xyz axes. These are then projected to camera view using the rotation matrix and translation vector.
		unitv_points = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1]], dtype = 'float32').reshape((4,1,3))
		if ret:
			points, jac = cv2.projectPoints(unitv_points, rvec, tvec, self.cmtx, self.dist)
			# print(rvec,":rvec\n", tvec,":tvec\n") 
			# rvec = np.array(rvec)
			# tvec = np.array(tvec)
			
			R, _ = cv2.Rodrigues(rvec)
			
			qr_tvec = R.T @ tvec
			coeff = self.z / qr_tvec[2]
			return points, rvec, tvec, coeff


		#return empty arrays if rotation and translation values not found
		else: return [], [], []

	def pose_generation(self, rvec, tvec, coeff):
		pose = PoseStamped()

		pose.pose.position.x = tvec[0][0] * coeff
		pose.pose.position.y = tvec[1][0] * coeff
		pose.pose.position.z = 0

		pose.pose.orientation.x,pose.pose.orientation.y,pose.pose.orientation.z,pose.pose.orientation.w = 0.707, -0.707, 0, 0
		# euler_to_quaternion(rvec[0][0], rvec[1][0], rvec[2][0])

		pose.header.frame_id = 'hummingbird/camera_hummingbird_optical_link'

		return pose
 
	

	def callback(self,data):
		bridge = CvBridge()

		try:
			cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
		except CvBridgeError as e:
			rospy.logerr(e)

		clean_img = np.copy(cv_image)

		# ret_qr, points = self.qr.detect(cv_image)
		decoded = self.qr(cv_image)

		# if ret_qr:
		if len(decoded):
			corners = np.array([[[pt.x, pt.y] for pt in decoded[0].polygon]], np.float32)
			axis_points, rvec, tvec, coeff = self.get_qr_coords(corners)
			# axis_points, rvec, tvec = self.get_qr_coords(points)

			pose = self.pose_generation(rvec, tvec, coeff)
			self.waypoint_pub.publish(pose)

			#BGR color format
			colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0,0,0)]

			#check axes points are projected to camera view.
			if len(axis_points) > 0:
				axis_points = axis_points.reshape((4,2))

				origin = (int(axis_points[0][0]),int(axis_points[0][1]) )

				for p, c in zip(axis_points[1:], colors[:3]):
					p = (int(p[0]), int(p[1]))

					#Sometimes qr detector will make a mistake and projected point will overflow integer value. We skip these cases. 
					if origin[0] > 5*cv_image.shape[1] or origin[1] > 5*cv_image.shape[1]:break
					if p[0] > 5*cv_image.shape[1] or p[1] > 5*cv_image.shape[1]:break

					cv2.line(cv_image, origin, p, c, 5)

		# else: rospy.logwarn(f'No Qr detected, Corners : {points}')
		else: rospy.logwarn(f'No Qr detected, Corners : {decoded}')
		
		cv2.imshow("Camera output", clean_img)
		cv2.imshow("Perception Output", cv_image)

		cv2.waitKey(1)
		# return image

def main():
	output = camera_hummingbird()
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
		rospy.loginfo("Shutting down")
	
	cv2.destroyAllWindows()

if __name__ == '__main__':
		rospy.init_node('camera_read', anonymous=False)
		main()