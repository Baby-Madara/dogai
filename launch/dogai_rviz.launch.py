#!/usr/bin/python3


import os
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()



    # Specify the name of the package and path to xacro file within the package
    # file_subpath = 'description/example_robot.urdf.xacro'
    pkg_name     = 'dogai'
    file_subpath = 'urdf/dogai.urdf'

    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Start rviz2
    node_rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', '~/ros2_ws/src/dogai/rviz/rviz_settings.rviz']
    )

    ld.add_action(node_rviz2)
    

    return ld