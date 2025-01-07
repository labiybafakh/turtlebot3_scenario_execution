#!/bin/bash

# Stop on any error
set -e

CURRENT_UID=$(id -u)
CURRENT_GID=$(id -g)
CURRENT_USER=$(whoami)

# Navigate to the workspace root (two directories up from the docker directory)
# cd "~/ros_ws"

# Check if container already exists
if [ "$(docker ps -aq -f name=turtlebot3_secenario_execution_container)" ]; then
    echo "Removing existing container..."
    docker rm -f turtlebot3_secenario_execution_container
fi

echo "Starting ROS Noetic container..."
docker run --rm -it --privileged \
       -v /etc/group:/etc/group:ro \
       -v /etc/passwd:/etc/passwd:ro \
       -u $(id -u):$(id -g) \
       --group-add=46 \
       -v /tmp/.X11-unix/:/tmp/.X11-unix \
       -e DISPLAY=${DISPLAY} \
    noetic:turtlebot3_scenario_execution

echo "Container stopped."