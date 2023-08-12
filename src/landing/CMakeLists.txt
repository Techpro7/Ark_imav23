cmake_minimum_required(VERSION 2.8.3)
project(landing)

find_package(catkin REQUIRED)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS 
  roscpp 
  gazebo_ros 
  geometry_msgs
  mav_msgs
  sensor_msgs
  xacro
)

# Depend on system install of Gazebo
find_package(gazebo REQUIRED)

catkin_package(
  DEPENDS 
    roscpp 
    gazebo_ros 
    xacro
    geometry_msgs
    mav_msgs
    sensor_msgs
)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})

find_package(rosinstall)
execute_process(COMMAND pip3 install pyzbar --ignore-installed --target=${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_PYTHON_DESTINATION})