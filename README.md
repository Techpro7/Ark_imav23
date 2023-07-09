# Ark_imav23
Simulation package

Download this package and put it in your catkin workspace

# How to run the simulaiton
The world folder contains all the world files the imav_2023_world file contains the static build of simulation enviornment.

The trial world file has a plugin attached to the rotating platform model (not working) 

The plugins are located in imav_plugins/src/ folder 

# If the models are not loaded

Open your .bashrc file and add 
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/path/to/your/models/folder/

If the trial file shows plugin not found or similar error
open the trial world file and search for <plugin> tag change the filename to wherever .so file is located in your system
