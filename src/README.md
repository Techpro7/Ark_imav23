# Ark_imav23
## imav_gazebo

This ROS package simulates the world for the IMAV 2023 competition using Gazebo.

## Installation

Follow the instructions below to set up the package:

1. Clone this repository into your ROS workspace's `src` folder.
2. Build the workspace using `catkin build` or `catkin_make`.
3. Source the package by running `source devel/setup.bash`.

## Usage

To launch the simulation environment, run the following command:

```bash
roslaunch imav_gazebo imav_world.launch
```
## Changing Angular Velocity of the Rotating Platform

To modify the angular velocity of the rotating platform, follow these steps:

1. Locate the `model.sdf` file for the rotating plate with the QR model. It is at `/imav_gazebo/models/rotating_plate_with_qr/model.sdf`.
2. Open the `model.sdf` file in a text editor.
3. Look for the `<vel>` tag in the file. It specifies the current angular velocity of the rotating platform.
4. Modify the value of the `<vel>` tag to the desired angular velocity.
5. Save the changes to the `model.sdf` file.

## Changing Parameters for SHM Motion of the Moving Window

To adjust the parameters for the Simple Harmonic Motion (SHM) of the moving window, follow these steps:

1. Locate the `model.sdf` file for the moving window model. It is at `/imav_gazebo/models/moving_window/model.sdf`.
2. Open the `model.sdf` file in a text editor.
3. Find the section that defines the SHM motion parameters for the moving obstacle.
4. Modify the desired parameters, such as the amplitude, frequency, or initial phase, offset according to your requirements.
5. Save the changes to the `model.sdf` file.


