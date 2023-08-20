from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cpp',
            executable='morioka_publisher',
            name='morioka_pub'
        ),
         Node(
            package='cpp',
            executable='morioka_subscriber',
            name='morioka_sub'
        ), Node(
            package='cpp',
            executable='saitama_broadcaster',
            name='saitama_broadcaster'
        ), Node(
            package='cpp',
            executable='saitama_receiver',
            name='saitama_receiver'
        ), 
    ])