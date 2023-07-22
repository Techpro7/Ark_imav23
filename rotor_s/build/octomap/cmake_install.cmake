# Install script for directory: /home/pranjal/rotor_s/src/octomap/octomap

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pranjal/rotor_s/devel")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/octomap" TYPE FILE FILES
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/AbstractOcTree.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/AbstractOccupancyOcTree.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/ColorOcTree.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/CountingOcTree.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/MCTables.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/MapCollection.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/MapCollection.hxx"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/MapNode.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/MapNode.hxx"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTree.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeBase.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeBaseImpl.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeBaseImpl.hxx"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeDataNode.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeDataNode.hxx"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeIterator.hxx"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeKey.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeNode.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OcTreeStamped.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OccupancyOcTreeBase.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/OccupancyOcTreeBase.hxx"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/Pointcloud.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/ScanGraph.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/octomap.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/octomap_deprecated.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/octomap_timing.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/octomap_types.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/octomap_utils.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/octomap/math" TYPE FILE FILES
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/math/Pose6D.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/math/Quaternion.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/math/Utils.h"
    "/home/pranjal/rotor_s/src/octomap/octomap/include/octomap/math/Vector3.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/octomap" TYPE FILE FILES "/home/pranjal/rotor_s/src/octomap/octomap/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/pranjal/rotor_s/build/octomap/share/ament_index/resource_index/packages/octomap")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/octomap" TYPE FILE FILES
    "/home/pranjal/rotor_s/build/octomap/InstallFiles/octomap-config.cmake"
    "/home/pranjal/rotor_s/build/octomap/InstallFiles/octomap-config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pranjal/rotor_s/build/octomap/lib/pkgconfig/octomap.pc")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/pranjal/rotor_s/build/octomap/src/math/cmake_install.cmake")
  include("/home/pranjal/rotor_s/build/octomap/src/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/pranjal/rotor_s/build/octomap/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
