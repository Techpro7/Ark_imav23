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
include src/testing/CMakeFiles/test_color_tree.dir/depend.make

# Include the progress variables for this target.
include src/testing/CMakeFiles/test_color_tree.dir/progress.make

# Include the compile flags for this target's objects.
include src/testing/CMakeFiles/test_color_tree.dir/flags.make

src/testing/CMakeFiles/test_color_tree.dir/test_color_tree.cpp.o: src/testing/CMakeFiles/test_color_tree.dir/flags.make
src/testing/CMakeFiles/test_color_tree.dir/test_color_tree.cpp.o: /home/pranjal/rotor_s/src/octomap/octomap/src/testing/test_color_tree.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pranjal/rotor_s/build/octomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/testing/CMakeFiles/test_color_tree.dir/test_color_tree.cpp.o"
	cd /home/pranjal/rotor_s/build/octomap/src/testing && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_color_tree.dir/test_color_tree.cpp.o -c /home/pranjal/rotor_s/src/octomap/octomap/src/testing/test_color_tree.cpp

src/testing/CMakeFiles/test_color_tree.dir/test_color_tree.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_color_tree.dir/test_color_tree.cpp.i"
	cd /home/pranjal/rotor_s/build/octomap/src/testing && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pranjal/rotor_s/src/octomap/octomap/src/testing/test_color_tree.cpp > CMakeFiles/test_color_tree.dir/test_color_tree.cpp.i

src/testing/CMakeFiles/test_color_tree.dir/test_color_tree.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_color_tree.dir/test_color_tree.cpp.s"
	cd /home/pranjal/rotor_s/build/octomap/src/testing && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pranjal/rotor_s/src/octomap/octomap/src/testing/test_color_tree.cpp -o CMakeFiles/test_color_tree.dir/test_color_tree.cpp.s

# Object files for target test_color_tree
test_color_tree_OBJECTS = \
"CMakeFiles/test_color_tree.dir/test_color_tree.cpp.o"

# External object files for target test_color_tree
test_color_tree_EXTERNAL_OBJECTS =

/home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree: src/testing/CMakeFiles/test_color_tree.dir/test_color_tree.cpp.o
/home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree: src/testing/CMakeFiles/test_color_tree.dir/build.make
/home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree: /home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomap.so.1.9.8
/home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree: /home/pranjal/rotor_s/src/octomap/octomap/lib/liboctomath.so.1.9.8
/home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree: src/testing/CMakeFiles/test_color_tree.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pranjal/rotor_s/build/octomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree"
	cd /home/pranjal/rotor_s/build/octomap/src/testing && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_color_tree.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/testing/CMakeFiles/test_color_tree.dir/build: /home/pranjal/rotor_s/src/octomap/octomap/bin/test_color_tree

.PHONY : src/testing/CMakeFiles/test_color_tree.dir/build

src/testing/CMakeFiles/test_color_tree.dir/clean:
	cd /home/pranjal/rotor_s/build/octomap/src/testing && $(CMAKE_COMMAND) -P CMakeFiles/test_color_tree.dir/cmake_clean.cmake
.PHONY : src/testing/CMakeFiles/test_color_tree.dir/clean

src/testing/CMakeFiles/test_color_tree.dir/depend:
	cd /home/pranjal/rotor_s/build/octomap && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pranjal/rotor_s/src/octomap/octomap /home/pranjal/rotor_s/src/octomap/octomap/src/testing /home/pranjal/rotor_s/build/octomap /home/pranjal/rotor_s/build/octomap/src/testing /home/pranjal/rotor_s/build/octomap/src/testing/CMakeFiles/test_color_tree.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/testing/CMakeFiles/test_color_tree.dir/depend

