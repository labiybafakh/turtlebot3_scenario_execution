cmake_minimum_required(VERSION 3.0.2)
project(turtlebot3_scenario_execution)

add_compile_options(-std=c++14)

find_package(catkin REQUIRED COMPONENTS
  rospy
  nav_msgs
  move_base_msgs
  actionlib
  actionlib_msgs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS
    nav_msgs
    move_base_msgs
    actionlib
    actionlib_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/yaml_to_nav.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)