import rospy

from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState

import tf2_ros
import tf2_geometry_msgs
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import PoseStamped, TransformStamped

import cv2

class Listener:
    def __init__(self, child_frame: str, waypoint_topic: str):
        rospy.init_node('topic_lafda')

        rospy.wait_for_service('/gazebo/set_model_state')
        self.vis = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

        self.rate = rospy.Timer(period = rospy.Duration(0.1), callback = self.pub_cb)
        
        self.pose_pub = rospy.Publisher('hummingbird/command/pose', PoseStamped)
        self.pose_sub = rospy.Subscriber(waypoint_topic, PoseStamped, self.waypoint_cb)

        self.child_frame = child_frame
        self.transform_sub = rospy.Subscriber('/tf', TFMessage, self.tf_cb)

        self.last_pose = None
        self.last_transform = None

        self.tf2_buff = tf2_ros.Buffer()
        self.tf2_listener = tf2_ros.TransformListener(self.tf2_buff)

    def waypoint_cb(self, msg: PoseStamped):
        self.last_pose = msg
    
    def pub_cb(self, _):
        if self.last_transform is None:
            return
        if self.last_pose is None:
            return
        
        transform = self.tf2_buff.lookup_transform('world', 'hummingbird/camera_hummingbird_optical_link', rospy.Time())

        global_pose = tf2_geometry_msgs.do_transform_pose(self.last_pose, transform)
        # global_pose = tf2_geometry_msgs.do_transform_pose(self.last_pose, self.last_transform)

        state_msg = ModelState()

        state_msg.model_name = 'unit_box'
        
        state_msg.pose = global_pose.pose

        self.vis(state_msg)
        
        # self.pose_pub.publish(global_pose)
    
    def tf_cb(self, msg: TFMessage):
        transform = msg.transforms[0]       

        if transform.child_frame_id == self.child_frame:
            self.last_transform = transform

# def pose_callback(pub: rospy.Publisher, msg: PoseStamped):
#     msg.header.frame_id = 'hummingbird/base_link'

#     tf2_buff = tf2_ros.Buffer()
#     listener = tf2_ros.TransformListener(tf2_buff)
    
#     try:
#         transform = tf2_buff.lookup_transform('world', msg.header.frame_id, rospy.Time(0))
#     except Exception as e:
#         rospy.logerr(e)
#         return

#     pose_transformed = tf2_geometry_msgs.do_transform_pose(msg, transform)
#     pub.publish(pose_transformed)

def main():
    listener = Listener('hummingbird/base_link', 'waypoint_topic')    

    rospy.spin()

if __name__ == '__main__':
    main()