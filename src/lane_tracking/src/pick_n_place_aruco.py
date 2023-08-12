#!/usr/bin/env python3


'''
This is a boiler plate script that contains hint about different services that are to be used
to complete the task.
Use this code snippet in your code or you can also continue adding your code in the same file


This python file runs a ROS-node of name pick_n_place which controls the drone in offboard mode, picks a package, places it at its destination and returns. 
See the documentation for offboard mode in px4 here() to understand more about offboard mode 
This node publishes and subsribes the following topics:

	Services to be called                   Publications                                          Subscriptions				
	/mavros/cmd/arming                      /mavros/setpoint_position/local                       /mavros/state
    /mavros/set_mode                        /mavros/setpoint_velocity/cmd_vel                     /mavros/local_position/pose   
    /activate_gripper                                                                             /gripper_check
         
    
'''

import math
from math import sqrt, tanh, exp
from time import time

import rospy
from geometry_msgs.msg import *
from mavros_msgs.msg import *
from mavros_msgs.srv import *
from rospy.impl.tcpros_service import ServiceProxy
from rospy.topics import Publisher, Subscriber
from gazebo_ros_link_attacher.srv import Gripper
from sensor_msgs.msg import Image
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import cv2
from cv2 import aruco

# Run mode tells whether the code has been added to launch file or run separately run in terminal
# It is neccesary because when we are running the code in launch file, we need to wait for a few seconds
# before checking for connection, in order for PX4 to settle down
# RUNMODE = 0 : It is run from launch file
# RUNMODE = 1 : It is run from separate terminal
RUNMODE = 1 # WARNING, MUST CHECK : Since I added this to my launch file. Kindly change it to 1 if you have not added it to the launch file

# Precision variable is important in setting the accuracy of path followed, but has an adversarial impact on time of flight
precision = 0.1 / (1.5 ** 0.33) # Idea behind using cube root is because it will be used for volume calculation.
linPrecision = 0.2 # Precision for linear calculations

## Target mode defines how it is checked that the drone has reached the setpoint/target
## TARGETMODE = 0 : It lies in a sphere of radius = precision, with center at the setpoint
## TARGETMODE = 1 : It lies in a precision x precision x precision cube, with center at the setpoint
## DEFAULTMODE is used when the mode given is out of the range of defined values
TARGETMODE = 0
DEFAULTTARGETMODE = 1

## Falloff mode defines the function used to lower velocity as the drone closes in on the setpoint
## TARGETMODE = 0 : Hyperbolic Tangent
## TARGETMODE = 1 : Sigmoid
## TARGETMODE = 2 : Linear
## DEFAULTMODE is used when the mode given is out of the range of defined values
FALLOFFMODE = 0
DEFAULTFALLOFFMODE = 1

# Fall off parameters
STARTFALLOFFAT = 0.03 # Start velocity fall off when 3% of the journey is left
ENDFALLOFFAT = 0.002 # continue constant value when 0.2 % of the journey is left

# FALLOFF : 
## Adding fall off to the velocity is helpful in avoiding overshooting and ensuring a fairly accurate path.
## If we keep on lowering precision arbitrarily then overshooting corrections will take ages and we have to compromise between time of flight and accuracy of the path
## That was the basic motivation behind adding a falloff to velocity
## As of now the only good falloff functions I could think of are Identity, Sigmoid and Hyperbolic Tan
## We will explore on other falloff functions in the coming tasks.

# Checking if destination is reached :
## Checking if the drone lies in a bounding cube of edge length l, vs a bounding sphere of radius precision makes a lot of difference
## If we are travelling along X axis, there will be fairly less error along Y and Z axes. and most of the error must be in X axis.
## We could use even custom bounding cuboid or ellipsoids that point in the direction of travel as that will be the direction of maximum error.
## We will explore on other bounding volumes in the coming tasks.

TIMEOUTTHRESH = 1

# Camera matrix and distortion coeffecients obtained from /eDrone/camera/camera_info rostopic
CAMMATRIX = np.array([238.3515418007097, 0.0, 200.5, 0.0, 238.3515418007097, 200.5, 0.0, 0.0, 1.0], dtype = np.float32).reshape((3, 3))
DISTORTIONCOEFFS = np.array([0, 0, 0, 0, 0], dtype = np.float32)
xPrecision = 0.001

class control:

    def __init__(self):
        # Initialise rosnode
        rospy.init_node('control', anonymous=True)
        
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
        self.parameters = aruco.DetectorParameters_create()

    def setFailSafe(self) -> None :
        # Calling to /mavros/param/set to disable failsafe for offboard and print fail message on failure
        rospy.wait_for_service('mavros/param/set')  # Waiting untill the service starts 
        try:
            paramService = rospy.ServiceProxy('mavros/param/set', ParamSet) # Creating a proxy service for the rosservice named /mavros/cmd/arming for arming the drone 
            paramid = 'COM_RCL_EXCEPT'
            paramvalue = ParamValue(integer = (1 << 9) - 1) # values stored bitwise. If you want to activate OFFBOARD, which is 2, you have to put 1 in 2nd index bit, i.e 1 << 2 = bin(1 0 0)
            paramService(paramid, paramvalue)        
        except rospy.ServiceException as e:
            print ("Service arming call failed: %s"%e)

    def setAccAllowance(self) -> None :
        # Calling to /mavros/param/set to disable failsafe for offboard and print fail message on failure
        rospy.wait_for_service('mavros/param/set')  # Waiting untill the service starts 
        try:
            paramService = rospy.ServiceProxy('mavros/param/set', ParamSet) # Creating a proxy service for the rosservice named /mavros/cmd/arming for arming the drone 
            paramid = 'COM_ARM_IMU_ACC'
            paramvalue = ParamValue(real = 0.7) # values stored bitwise. If you want to activate OFFBOARD, which is 2, you have to put 1 in 2nd index bit, i.e 1 << 2 = bin(1 0 0)
            paramService(paramid, paramvalue)        
        except rospy.ServiceException as e:
            print ("Service arming call failed: %s"%e)
    
    def setArm(self) -> None:
        # Calling to /mavros/cmd/arming to arm the drone and print fail message on failure
        rospy.wait_for_service('mavros/cmd/arming')  # Waiting untill the service starts 
        try:
            armService = rospy.ServiceProxy('mavros/cmd/arming', mavros_msgs.srv.CommandBool) # Creating a proxy service for the rosservice named /mavros/cmd/arming for arming the drone 
            armService(True) # Arm
        except rospy.ServiceException as e:
            print ("Service arming call failed: %s"%e)

        # Similarly declare other service proxies 

    def setDisArm(self) -> None:
        # Calling to /mavros/cmd/arming to disarm the drone and print fail message on failure
        rospy.wait_for_service('mavros/cmd/arming')  # Waiting untill the service starts 
        try:
            armService = rospy.ServiceProxy('mavros/cmd/arming', mavros_msgs.srv.CommandBool) # Creating a proxy service for the rosservice named /mavros/cmd/arming for arming the drone 
            armService(False) # Disarm
        except rospy.ServiceException as e:
            print ("Service arming call failed: %s"%e)

    def offboard_set_mode(self) -> None:
        # Call /mavros/set_mode to set the mode the drone to OFFBOARD
        # and print fail message on failure

        rospy.wait_for_service('mavros/set_mode')  # Waiting untill the service starts 
        # msg = SetMode()._request_class
        msg = SetModeRequest()
        msg.base_mode = 0                           # 0 is custom mode.
        msg.custom_mode = 'OFFBOARD'
        try:
            modeService = rospy.ServiceProxy('mavros/set_mode', SetMode) # Creating a proxy service for the rosservice named /mavros/set_mode to set the mode the drone to OFFBOARD 
            modeService(msg)
        except rospy.ServiceException as e:
            print ("Service set mode call failed: %s"%e)

    def land_set_mode(self) -> None :
        # Call /mavros/set_mode to set the mode the drone to OFFBOARD
        # and print fail message on failure

        rospy.wait_for_service('mavros/set_mode')  # Waiting untill the service starts 
        # msg = SetMode()._request_class
        msg = SetModeRequest()
        msg.base_mode = 0                           # 0 is custom mode.
        msg.custom_mode = 'AUTO.LAND'
        try:
            modeService = rospy.ServiceProxy('mavros/set_mode', SetMode) # Creating a proxy service for the rosservice named /mavros/set_mode to set the mode the drone to OFFBOARD 
            modeService(msg)
        except rospy.ServiceException as e:
            print ("Service set mode call failed: %s"%e)
    
    def land_set_mode(self) -> None:
        # Call /mavros/set_mode to set the mode the drone to OFFBOARD
        # and print fail message on failure

        rospy.wait_for_service('mavros/set_mode')  # Waiting untill the service starts 
        # msg = SetMode()._request_class
        msg = SetModeRequest()
        msg.base_mode = 0                           # 0 is custom mode.
        msg.custom_mode = 'AUTO.LAND'
        try:
            modeService = rospy.ServiceProxy('mavros/set_mode', SetMode) # Creating a proxy service for the rosservice named /mavros/set_mode to set the mode the drone to OFFBOARD 
            modeService(msg)
        except rospy.ServiceException as e:
            print ("Service set mode call failed: %s"%e)
    def gripper(self, arg : bool) -> bool :
        assert type(arg) is bool
        # Call /activate_gripper to pick/place depending on the arg passed
        # arg : True        -> pick
        # ard : False       -> place

        rospy.wait_for_service('/activate_gripper')  # Waiting untill the service starts 
        msg = arg
        try:
            gripperService = rospy.ServiceProxy('/activate_gripper', Gripper) # Creating a proxy service for the rosservice named /mavros/set_mode to set the mode the drone to OFFBOARD 
            retVal = gripperService(msg)
            return retVal.result
             
        except rospy.ServiceException as e:
            print ("Service activate gripper call failed: %s"%e)
   
class stateMoniter:
    def __init__(self):
        self.state = State()
        # Instantiate a setpoints message
        self.x = 0
        self.y = 0
        self.z = 0
        self.canPick = std_msgs.msg.String()
        self.bridge = CvBridge()
        self.img = np.empty([])
        
    def stateCb(self, msg : State) -> None:
        # Callback function for topic /mavros/state
        self.state = msg

    # Create more callback functions for other subscribers    
    def posiCallBack(self, msg : PoseStamped) -> None :
        # Stores current position of the drone to the monitor instance
        self.x = msg.pose.position.x
        self.y = msg.pose.position.y
        self.z = msg.pose.position.z
    def gripperCallBack(self, msg : std_msgs.msg.String) -> None :
        self.canPick = msg
    def camCallBack(self, msg : Image) :
        try :
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as err :
            print(err)

def fallOff(val : float, _mode : int = None) -> float : 
    # Using a falloff function of  choice.
    # The input value is in the range of 0 - 1 and output is in the range of 0 - 1 where as we approach 0, the output falls off rapidly
    # More details in line 47
    global FALLOFFMODE
    global DEFAULTFALLOFFMODE
    prevMode = FALLOFFMODE # Save the mode
    if _mode is not None : # if some mode is given in arguments, use that mode 
        FALLOFFMODE = _mode
    if FALLOFFMODE == 0 :
        FALLOFFMODE = prevMode
        return tanh(val) / tanh(1)
    elif FALLOFFMODE == 1 : 
        FALLOFFMODE = prevMode
        return (sigmoid(val) - 0.5) / (sigmoid(1) - 0.5)
    elif FALLOFFMODE == 2 : 
        FALLOFFMODE = prevMode
        return val    
    else :
        return reachedDestination(val, _mode = DEFAULTFALLOFFMODE)

def velFallOff(stateMt : stateMoniter, setpoints : list, i : int) -> Twist : 
    # Reduces the velocity as we approach the target, using a falloff function
    # More details in line 59
    assert i > 0
    pos = setpoints[i][0]
    _pos = setpoints[i - 1][0]
    total = sqrt((pos.pose.position.x - _pos.pose.position.x) ** 2 + (pos.pose.position.y - stateMt.y) ** 2 + (pos.pose.position.z- _pos.pose.position.z) ** 2)
    left =  sqrt((pos.pose.position.x - stateMt.x) ** 2 + (pos.pose.position.y - stateMt.y) ** 2 + (pos.pose.position.z - stateMt.z) ** 2)

    newVel = setpoints[i][1]

    tup = (newVel.linear.x, newVel.linear.y, newVel.linear.z)
    ratio = left / total
    ratio = max(ratio, ENDFALLOFFAT)

    if ratio < STARTFALLOFFAT :
        multiplier = fallOff(ratio / STARTFALLOFFAT)

        x = tup[0] * multiplier
        y = tup[1] * multiplier
        z = tup[2] * multiplier

        newVel.linear.x = x
        newVel.linear.y = y
        newVel.linear.z = z
    return newVel

def sigmoid(x : float) -> float : 
    # Defining signmoid function as it it not there in math library
    z = exp(-x)
    return 1 / (1 + z)

def reachedDestination(stateMt : stateMoniter, targetCoordinates : tuple, _mode = None) -> bool :
    # Checks if the drone has reached the current target, given the precision values and checking mode
    # More details in line 40 and 66
    global TARGETMODE
    global DEFAULTTARGETMODE
    prevMode = TARGETMODE
    if _mode is not None :
        TARGETMODE = _mode
    if TARGETMODE == 0 : 
        TARGETMODE = prevMode
        rad = sqrt((stateMt.x - targetCoordinates[0]) ** 2 + (stateMt.y - targetCoordinates[1]) ** 2 + (stateMt.z - targetCoordinates[2]) ** 2)
        return rad < precision
    elif TARGETMODE == 1 : 
        TARGETMODE = prevMode
        return abs(stateMt.x - targetCoordinates[0]) < (precision / 2) and abs(stateMt.y - targetCoordinates[1]) < (precision / 2) and abs(stateMt.z - targetCoordinates[2]) < (precision / 2)
    else :
        return reachedDestination(targetCoordinates, _mode = DEFAULTTARGETMODE)

def addSetpoint(coords : tuple, velocity : tuple, setpoints : list) -> None :
    # Neatly adds setpoints, given coordinates and velocity vector
    # coords must be a 3D tuple having x, y, z values
    # velocity must be likewise a 3D tuple having linear velocity componenets along x, y and z axes.
    # setpoints is the global list of setpoints
    
    # Set your position here
    pos = PoseStamped()
    pos.pose.position.x, pos.pose.position.y, pos.pose.position.z = coords

    # Set your velocity here
    vel = Twist()
    vel.linear.x, vel.linear.y, vel.linear.z = velocity

    setpoints.append((pos, vel))

def coverSetpoints(setpointsIndices : list, setpoints : list, stateMt : stateMoniter, local_pos_pub : Publisher, local_vel_pub : Publisher, rate : rospy.Rate, ctl : control, paramState : ServiceProxy, findingTarget = True) -> None :
    for setpoint in setpointsIndices :
        while not rospy.is_shutdown() :
            # If reached the setpoint, move to next setpoint

            if stateMt.state.mode != "OFFBOARD" :
                # Auto correction code here
                print('Accelerometer error. Trying it get it back to offboard as soon as it is fixed.')
                # The idea is to try and stall around
                currentPosSetpoint = PoseStamped(), Twist()
                currentPosSetpoint[0].pose.position.x = stateMt.x
                currentPosSetpoint[0].pose.position.y = stateMt.y
                currentPosSetpoint[0].pose.position.z = stateMt.z

                currentPosSetpoint[1].linear.x, currentPosSetpoint[1].linear.y, currentPosSetpoint[1].linear.z = 0, 0, 0

                enterOffboard(currentPosSetpoint, stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

            if reachedDestination(stateMt, (setpoints[setpoint][0].pose.position.x, setpoints[setpoint][0].pose.position.y, setpoints[setpoint][0].pose.position.z)) :
                break
            
            # Publish position
            local_pos_pub.publish(setpoints[setpoint][0])
            # Publish velocity
            _vel = velFallOff(stateMt, setpoints, setpoint)
            local_vel_pub.publish(_vel)

            found, Camtvec = scan(ctl, stateMt)

            if found and findingTarget : 
                break
            
            rate.sleep()

    if not findingTarget :
        land(ctl, stateMt, rate)
        return

    currentPosSetpoint = PoseStamped(), Twist()
    currentPosSetpoint[0].pose.position.x = stateMt.x + Camtvec[0]
    currentPosSetpoint[0].pose.position.y = stateMt.y - Camtvec[1] + 0.2
    currentPosSetpoint[0].pose.position.z = stateMt.z

    currentPosSetpoint[1].linear.x, currentPosSetpoint[1].linear.y, currentPosSetpoint[1].linear.z = 0, 0, 0

    while not rospy.is_shutdown() and not reachedDestination(stateMt, (currentPosSetpoint[0].pose.position.x, currentPosSetpoint[0].pose.position.y, currentPosSetpoint[0].pose.position.z)) :
        if stateMt.state.mode != "OFFBOARD" :
            # Auto correction code here
            print('Accelerometer error. Trying it get it back to offboard as soon as it is fixed.')
            # The idea is to try and stall around
            
            currentPosSetpoint = PoseStamped(), Twist()
            currentPosSetpoint[0].pose.position.x = stateMt.x
            currentPosSetpoint[0].pose.position.y = stateMt.y
            currentPosSetpoint[0].pose.position.z = stateMt.z

            currentPosSetpoint[1].linear.x, currentPosSetpoint[1].linear.y, currentPosSetpoint[1].linear.z = 0, 0, 0

            enterOffboard(currentPosSetpoint, stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

        # Publish position
        local_pos_pub.publish(currentPosSetpoint[0])
        # Publish velocity
        _vel = velFallOff(stateMt, setpoints, setpoint)
        local_vel_pub.publish(currentPosSetpoint[1])

        found = scan(ctl, stateMt)

        rate.sleep()

    currentPosSetpoint = PoseStamped(), Twist()
    currentPosSetpoint[0].pose.position.x = stateMt.x
    currentPosSetpoint[0].pose.position.y = stateMt.y
    currentPosSetpoint[0].pose.position.z = 1

    currentPosSetpoint[1].linear.x, currentPosSetpoint[1].linear.y, currentPosSetpoint[1].linear.z = 0, 0, 0

    while not rospy.is_shutdown() :
        
        while not rospy.is_shutdown() and not reachedDestination(stateMt, (currentPosSetpoint[0].pose.position.x, currentPosSetpoint[0].pose.position.y, currentPosSetpoint[0].pose.position.z)) :
            if stateMt.state.mode != "OFFBOARD" :
                # Auto correction code here
                print('Accelerometer error. Trying it get it back to offboard as soon as it is fixed.')
                # The idea is to try and stall around
                
                currentPosSetpoint = PoseStamped(), Twist()
                currentPosSetpoint[0].pose.position.x = stateMt.x
                currentPosSetpoint[0].pose.position.y = stateMt.y
                currentPosSetpoint[0].pose.position.z = stateMt.z

                currentPosSetpoint[1].linear.x, currentPosSetpoint[1].linear.y, currentPosSetpoint[1].linear.z = 0, 0, 0

                enterOffboard(currentPosSetpoint, stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

            # Publish position
            local_pos_pub.publish(currentPosSetpoint[0])
            # Publish velocity
            _vel = velFallOff(stateMt, setpoints, setpoint)
            local_vel_pub.publish(currentPosSetpoint[1])

            found = scan(ctl, stateMt)

            rate.sleep()
        
        land(ctl, stateMt, rate)

        print("Landing correct ? ", stateMt.canPick.data)

        if stateMt.canPick.data == 'True' :
            break

        print('Bad landing, taking off again')

        enterOffboard(currentPosSetpoint, stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

def enterOffboard(dummySetpoint : tuple, stateMt : stateMoniter, ctl : control, paramState : rospy.ServiceProxy, local_pos_pub : Publisher, local_vel_pub : Publisher, rate : rospy.Rate) -> None :
    # Switching the state to offboard
    while not rospy.is_shutdown() : 
        # ctl.setAccAllowance()
        # print('Nothings wrong')
        if not stateMt.state.armed : 
            ctl.setArm()
        if not ((paramState('COM_RCL_EXCEPT').value.integer >> 2) & 1) : 
            ctl.setFailSafe()
            # print('Failsafe deactivat much')
        if not stateMt.state.mode == "OFFBOARD" :
            ctl.offboard_set_mode()
        else :
            break

        local_pos_pub.publish(dummySetpoint[0])
        local_vel_pub.publish(dummySetpoint[1])
        
        rate.sleep()

    print ("OFFBOARD mode activated")

def scan(ctl : control, stateMt : stateMoniter) -> tuple :
    '''Pose estimation of aruco tag on self.img'''
    gray_img = cv2.cvtColor(stateMt.img, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = aruco.detectMarkers(gray_img, ctl.aruco_dict, parameters = ctl.parameters)
    
    img = stateMt.img.copy()

    found = False
    Camtvec = None

    if ids != None :
        rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[0], 0.02, CAMMATRIX, DISTORTIONCOEFFS)
        
        # Draw a square around the markers
        cv2.aruco.drawDetectedMarkers(img, corners) 

        # Draw Axis
        cv2.aruco.drawAxis(img, CAMMATRIX, DISTORTIONCOEFFS, rvec, tvec, 0.01) 

        R, _ = cv2.Rodrigues(rvec)
        # print(R)

        Camrvec, _ = cv2.Rodrigues(R.T)

        Camtvec = - R.T @ tvec[0][0]

        coeff = stateMt.z / Camtvec[2] # 7.5

        Camtvec *= coeff

        # print(coeff)

        if abs(Camtvec[0]) <= 0.1 :
            found = True

        _id = ids[0][0]
        corners = corners[0][0]
        center = 0.5 * (corners[0] + corners[2])
        ctl.aruco_id = _id
        tl = corners[0]
        tr = corners[1]

        vector = (tr - tl)

        if vector[0] == 0 : 
            angle = [90, 270][vector[1] < 0]
        elif vector[1] == 0 : 
            angle = [0, 180][vector[0] < 0]
        else :
            angle = math.degrees(math.atan(vector[1] / vector[0]))
            angle = [180 + angle, angle][vector[0] > 0]
        
        ctl.yaw = (-angle + 90) % 360
        ctl.x = center[0]
        ctl.y = center[1]

        ## function to mark ArUco in the test image as per the instructions given in problem statement
        ## arguments: img is the test image 
        ##			  Detected_ArUco_markers is the dictionary returned by function detect_ArUco(img)
        ##			  ArUco_marker_angles is the return value of Calculate_orientation_in_degree(Detected_ArUco_markers)
        ## return: image namely img after marking the aruco as per the instruction given in problem statement

        ## enter your code here ##
        distance = 40

        center = 0.5 * (corners[0] + corners[2])

        cv2.circle(img, tuple(corners[0].astype(int)), 1, (125, 125, 125), -1)
        cv2.circle(img, tuple(corners[1].astype(int)), 1, (  0, 255,   0), -1)
        cv2.circle(img, tuple(corners[2].astype(int)), 1, (180, 105, 255), -1)
        cv2.circle(img, tuple(corners[3].astype(int)), 1, (255, 255, 255), -1)

        cv2.circle(img, tuple(center.astype(int)),     1, (  0,   0, 255), -1)

        cv2.line(img, tuple(center.astype(int)), tuple((0.5 * (corners[0] + corners[1])).astype(int)), (255,   0,   0), 1)

        cv2.putText(img, str(int(ctl.yaw)), tuple((center - np.array([distance, 0])).astype(int)),     cv2.FONT_HERSHEY_SIMPLEX, 0.33, (  0, 255,   0), 1)
        cv2.putText(img, str(ctl.aruco_id), tuple((center + np.array([distance / 4, 0])).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (  0,   0, 255), 1)        

    cv2.imshow("Cam", img)
    cv2.waitKey(2)

    return found, Camtvec

def land(ctl : control, stateMt : stateMoniter, rate : rospy.Rate) -> None :
    while not rospy.is_shutdown() :
        if not stateMt.state.mode == "AUTO.LAND" :
            ctl.land_set_mode()
        else :
            break
            
        rate.sleep()

    print ("Land mode activated")

    while not rospy.is_shutdown() :
        if stateMt.state.armed :
            scan(ctl, stateMt)
            ctl.setDisArm()
            rate.sleep()
        else :
            break
    
    print('Landed')

def main() -> None:

    stateMt = stateMoniter()
    ctl = control()

    rospy.Subscriber('/mavros/local_position/pose', PoseStamped, stateMt.posiCallBack)
    rospy.Subscriber('/gripper_check', std_msgs.msg.String, stateMt.gripperCallBack)
    Subscriber('eDrone/camera/image_raw', Image, stateMt.camCallBack)

    # Initialize publishers
    local_pos_pub = rospy.Publisher('mavros/setpoint_position/local', PoseStamped, queue_size=10)
    local_vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel', Twist, queue_size=10)
    
    # Specify the rate 
    rate = rospy.Rate(20.0)

    # Make the list of setpoints 
    setpoints = [] #List to setpoints

    # Create Setpoints
    addSetpoint((0, 0, 0), (0, 0, 0), setpoints)                # Empty setpoint                            
    addSetpoint((0, 0, 1), (0, 0, 3), setpoints)                # Takeoff setpoint                             -
    addSetpoint((1, 0, 1), (1, 0, 0), setpoints)                # 1st setpoint                                  |   Before picking up the object
    addSetpoint((2, 0, 1), (1, 0, 0), setpoints)                # 2nd setpoint
    addSetpoint((3, 0, 1), (1, 0, 0), setpoints)                # 3rd setpoint
    addSetpoint((4, 0, 1), (1, 0, 0), setpoints)                # 4th setpoint
    addSetpoint((5, 0, 1), (1, 0, 0), setpoints)                # 5th setpoint
    addSetpoint((6, 0, 1), (1, 0, 0), setpoints)                # 6th setpoint
    addSetpoint((7, 0, 1), (1, 0, 0), setpoints)                # 7th setpoint
    addSetpoint((8, 0, 1), (1, 0, 0), setpoints)                # 8th setpoint
    addSetpoint((9, 0, 1), (1, 0, 0), setpoints)                # 9th setpoint
    # addSetpoint((3, 0, 0), (0, 0, -3), setpoints)               # Land to pick setpoint                        -
    # addSetpoint((3, 0, 3), (3, 0, 0), setpoints)                # Takeoff setpoint                             -
    # addSetpoint((3, 3, 3), (0, 3, 0), setpoints)                # 2nd setpoint                                  |   After picking up the object
    # addSetpoint((3, 3, 0), (0, 0, -3), setpoints)               # Land to drop setpoint                        -
    # addSetpoint((3, 3, 3), (0, 0, 3), setpoints)                # Takeoff setpoint                             -
    # x = -3 / sqrt(2) #                                                                                          |
    # addSetpoint((0, 0, 3), (x, x, 0), setpoints)                # 3rd setpoint                                  |   Remaining
    # addSetpoint((0, 0, 0), (0, 0, -3), setpoints)               # Land setpoint                                -

    # Initialize subscriber 
    rospy.Subscriber("/mavros/state",State, stateMt.stateCb)

    # Service proxy
    # Calling to /mavros/param/get to get the param value and check if failsafe has been disabled successfully
    paramState = rospy.ServiceProxy('mavros/param/get', ParamGet) # Creating a proxy service for the rosservice named /mavros/cmd/arming for arming the drone

    if RUNMODE == 0 : # sleeps for 5 seconds in order to let PX4 settle down, when run from launch file
        rospy.loginfo('Sleeping')
        rospy.sleep(5)

    while not stateMt.state.connected :
        rate.sleep()

    print('Connected now')

    rospy.sleep(2)

    '''
    NOTE: To set the mode as OFFBOARD in px4, it needs some setpoints to be already published at rate > 10 hz, so before changing the mode to OFFBOARD, send some dummy setpoints.  
    '''
    for i in range(100) : # Here 100 has been taken as in the documentation too 100 were taken.
        local_pos_pub.publish(setpoints[0][0])
        local_vel_pub.publish(setpoints[0][1])
        rate.sleep()

    print('Published dummy set points')
    
    enterOffboard(setpoints[0], stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

    '''
    Testing purpose, may be removed
    pos = PoseStamped()
    pos.pose.position.x = 0
    pos.pose.position.y = 0
    pos.pose.position.z = 10
    while not rospy.is_shutdown() :
        local_pos_pub.publish(pos)
        local_vel_pub.publish(vel)
        rate.sleep()
    '''

    '''
    Step 1: Set the setpoint 
    Step 2: Then wait till the drone reaches the setpoint, 
    Step 3: Check if the drone has reached the setpoint by checking the topic /mavros/local_position/pose 
    Step 4: Once the drone reaches the setpoint, publish the next setpoint , repeat the process until all the setpoints are done  

    Write your algorithm here 
    '''

    # setpointsBeforePick = [1, 2, 3]
    # setpointsAfterPick = [4, 5, 6]
    # setpointsAfterDropping = [7, 8, 9]
    setpointsIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    coverSetpoints(setpointsIndices, setpoints, stateMt, local_pos_pub, local_vel_pub, rate, ctl, paramState)

    done = False
    while not rospy.is_shutdown() and not done :
        done = ctl.gripper(True)

    # while not rospy.is_shutdown() :
        
        newSet = []
        
    addSetpoint((stateMt.x, stateMt.y, stateMt.z), (0, 0, 0), newSet)    
    addSetpoint((stateMt.x, stateMt.y, 1), (0, 0, 3), newSet)
    addSetpoint((9, 0, 1), (0, 0, 0), newSet)

    enterOffboard(newSet[0], stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

    coverSetpoints([1, 2], newSet, stateMt, local_pos_pub, local_vel_pub, rate, ctl, paramState, findingTarget = False)

        # if reachedDestination(stateMt, (9, 0, 0), 1) :
        #     break

        # print('Bad landing, taking off again')

    done = False
    while not rospy.is_shutdown() and not done :
        done = not ctl.gripper(False)

    

    # while not rospy.is_shutdown() :
    
    newSet = []
    
    addSetpoint((stateMt.x, stateMt.y, stateMt.z), (0, 0, 0), newSet)    
    addSetpoint((stateMt.x, stateMt.y, 1), (0, 0, 3), newSet)
    addSetpoint((0, 0, 1), (0, 0, 0), newSet)

    enterOffboard(newSet[0], stateMt, ctl, paramState, local_pos_pub, local_vel_pub, rate)

    coverSetpoints([1, 2], newSet, stateMt, local_pos_pub, local_vel_pub, rate, ctl, paramState, findingTarget = False)

        # if reachedDestination(stateMt, (0, 0, 0), 1) :
        #     break

        # print('Bad landing, taking off again')

    # land(ctl, stateMt, rate)

    # print('Landed, Disarming now.')

    # # Disarming the drone
    # while stateMt.state.armed:
    #     ctl.setDisArm()
    #     rate.sleep()

    # print(stateMt.state.mode)

    # print("Disarmed!!")

#      238.3515418007097     , 0.0              , 200.5,
# K =  0.0                   , 238.3515418007097, 200.5,
#      0.0                   , 0.0              , 1.0
# D = [0, 0, 0, 0, 0]

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass