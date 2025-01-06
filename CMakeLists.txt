cmake_minimum_required(VERSION 3.0.2)
project(turtlebot3_scenario_execution)

add_compile_options(-std=c++14)

find_package(catkin REQUIRED)
catkin_package(
  INCLUDE_DIRS include

)

include_directories(
  include
)


install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)