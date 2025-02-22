import os
from launch import LaunchDescription
from launch_ros.actions import Node
import yaml

moveit_config = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), 'moveit_config_dump.yaml')))
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='xarm_moveit_config',  # Replace with your package name
            executable='pick_place',       # Replace with your node's executable name
            output="screen",
        parameters=[
            moveit_config
        ],
        )
        
    ])
