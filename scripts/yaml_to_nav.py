import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs import *
import yaml
import rospkg
from enum import Enum

MovingType = Enum('MovingType', ['ROTATE', 'STRAIGHT'])


def load_movement_config(yaml_file):
    try:
        with open(yaml_file, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except Exception as e:
        rospy.logerr(f"Error loading YAML file: {str(e)}")
        return None
    
def process_movements(config):
    index_waypoint = 0
    for item in config:
        if 'name' in item:
            print(f"Movement name: {item['name']}")
        if 'unit_moves' in item:
            moves = item['unit_moves']
            if not moves:  # Check if there are no moves
                print("No movements defined")
                return
                
            for move in moves:
                index_waypoint+=1

                print("\nWaypoint-"+ str(index_waypoint))
                print(f"Type: {move['moving_type']}")
                print(f"Direction: {move['direction']}")
                print(f"Speed: {move['speed']}")
                
                if move['moving_type'] == 'rotate':
                    print(f"Target angle: {move['target']['angle']} deg")
                elif move['moving_type'] == 'straight':
                    print(f"Target distance: {move['target']['distance']} m")
                
def main():
    rospy.init_node('multi_goal_navigation')
    movebase_action = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    movebase_action.wait_for_server()

    rospack = rospkg.RosPack()
    rospack.list() 
    path = rospack.get_path('turtlebot3_scenario_execution')

    config = load_movement_config(path + '/config/waypoint.yaml')
    process_movements(config)


    while True:
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 2.0
        goal.target_pose.pose.position.y = 0.0
        goal.target_pose.pose.position.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0

        movebase_action.send_goal(goal)


while not rospy.is_shutdown ():
    main()