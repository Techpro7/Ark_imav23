# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pranjal/rotor_s/src/octomap/octomap

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pranjal/rotor_s/build/octomap

# Include any dependencies generated for this target.
include src/math/CMakeFiles/octomath-static.dir/depend.make

# Include the progress variables for this target.
include src/math/CMakeFiles/octomath-static.dir/progress.make

# Include the compile flags for this target's objects.
include src/math/CMakeFiles/octomath-static.dir/flags.make

src/math/CMakeFiles/octomath-static.dir/Vector3.cpp.o: src/math/CMakeFiles/octomath-static.dir/flags.make
src/math/CMakeFiles/octomath-static.dir/Vector3.cpp.o: /home/pranjal/rotor_s/src/octomap/octomap/src/math/Vector3.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pranjal/rotor_s/build/octomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/math/CMakeFiles/octomath-static.dir/Vector3.cpp.o"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/octomath-static.dir/Vector3.cpp.o -c /home/pranjal/rotor_s/src/octomap/octomap/src/math/Vector3.cpp

src/math/CMakeFiles/octomath-static.dir/Vector3.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/octomath-static.dir/Vector3.cpp.i"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pranjal/rotor_s/src/octomap/octomap/src/math/Vector3.cpp > CMakeFiles/octomath-static.dir/Vector3.cpp.i

src/math/CMakeFiles/octomath-static.dir/Vector3.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/octomath-static.dir/Vector3.cpp.s"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pranjal/rotor_s/src/octomap/octomap/src/math/Vector3.cpp -o CMakeFiles/octomath-static.dir/Vector3.cpp.s

src/math/CMakeFiles/octomath-static.dir/Quaternion.cpp.o: src/math/CMakeFiles/octomath-static.dir/flags.make
src/math/CMakeFiles/octomath-static.dir/Quaternion.cpp.o: /home/pranjal/rotor_s/src/octomap/octomap/src/math/Quaternion.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pranjal/rotor_s/build/octomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/math/CMakeFiles/octomath-static.dir/Quaternion.cpp.o"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/octomath-static.dir/Quaternion.cpp.o -c /home/pranjal/rotor_s/src/octomap/octomap/src/math/Quaternion.cpp

src/math/CMakeFiles/octomath-static.dir/Quaternion.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/octomath-static.dir/Quaternion.cpp.i"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pranjal/rotor_s/src/octomap/octomap/src/math/Quaternion.cpp > CMakeFiles/octomath-static.dir/Quaternion.cpp.i

src/math/CMakeFiles/octomath-static.dir/Quaternion.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/octomath-static.dir/Quaternion.cpp.s"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pranjal/rotor_s/src/octomap/octomap/src/math/Quaternion.cpp -o CMakeFiles/octomath-static.dir/Quaternion.cpp.s

src/math/CMakeFiles/octomath-static.dir/Pose6D.cpp.o: src/math/CMakeFiles/octomath-static.dir/flags.make
src/math/CMakeFiles/octomath-static.dir/Pose6D.cpp.o: /home/pranjal/rotor_s/src/octomap/octomap/src/math/Pose6D.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pranjal/rotor_s/build/octomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/math/CMakeFiles/octomath-static.dir/Pose6D.cpp.o"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/octomath-static.dir/Pose6D.cpp.o -c /home/pranjal/rotor_s/src/octomap/octomap/src/math/Pose6D.cpp

src/math/CMakeFiles/octomath-static.dir/Pose6D.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/octomath-static.dir/Pose6D.cpp.i"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pranjal/rotor_s/src/octomap/octomap/src/math/Pose6D.cpp > CMakeFiles/octomath-static.dir/Pose6D.cpp.i

src/math/CMakeFiles/octomath-static.dir/Pose6D.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/octomath-static.dir/Pose6D.cpp.s"
	cd /home/pranjal/rotor_s/build/octomap/src/math && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pranjal/rotor_s/src/octomap/octomap/src/math/Pose6D.cpp -o CMakeFiles/octomath-static.dir/Pose6D.cpp.s

# Object files for target octomath-static
octomath__static_OBJECTS = \
"CMakeFiles/octomath-static.dir/Vector3.cpp.o" \
"CMakeFiles/octomath-static.dir/Quaternion.cpp.o" \
"CMakeFiles/octomath-static.dir/Pose6D.cpp.o"

# External object files for target octomath-static
octomath__static_EXTERNAL_OBJECTS =

/home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a: src/math/CMakeFiles/octomath-static.dir/Vector3.cpp.o
/home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a: src/math/CMakeFiles/octomath-static.dir/Quaternion.cpp.o
/home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a: src/math/CMakeFiles/octomath-static.dir/Pose6D.cpp.o
/home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a: src/math/CMakeFiles/octomath-static.dir/build.make
/home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a: src/math/CMakeFiles/octomath-static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pranjal/rotor_s/build/octomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX static library /home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a"
	cd /home/pranjal/rotor_s/build/octomap/src/math && $(CMAKE_COMMAND) -P CMakeFiles/octomath-static.dir/cmake_clean_target.cmake
	cd /home/pranjal/rotor_s/build/octomap/src/math && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/octomath-static.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/math/CMakeFiles/octomath-static.dir/build: /home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.a

.PHONY : src/math/CMakeFiles/octomath-static.dir/build

src/math/CMakeFiles/octomath-static.dir/clean:
	cd /home/pranjal/rotor_s/build/octomap/src/math && $(CMAKE_COMMAND) -P CMakeFiles/octomath-static.dir/cmake_clean.cmake
.PHONY : src/math/CMakeFiles/octomath-static.dir/clean

src/math/CMakeFiles/octomath-static.dir/depend:
	cd /home/pranjal/rotor_s/build/octomap && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pranjal/rotor_s/src/octomap/octomap /home/pranjal/rotor_s/src/octomap/octomap/src/math /home/pranjal/rotor_s/build/octomap /home/pranjal/rotor_s/build/octomap/src/math /home/pranjal/rotor_s/build/octomap/src/math/CMakeFiles/octomath-static.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/math/CMakeFiles/octomath-static.dir/depend

