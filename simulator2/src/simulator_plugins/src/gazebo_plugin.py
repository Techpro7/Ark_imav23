#!/usr/bin/env python3
import rospy
from gazebo_msgs.msg import ModelStates

def callback(msg):
    # Access the model states and perform desired operations
    # For example, print the position of the first model
    print(msg.pose[0].position)

def listener():
    # Initialize the ROS node
    rospy.init_node('gazebo_plugin', anonymous=True)

    # Subscribe to the ModelStates topic to receive updates about the models in the simulation
    rospy.Subscriber('/gazebo/model_states', ModelStates, callback)

    # Spin the ROS node to receive and process messages
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
