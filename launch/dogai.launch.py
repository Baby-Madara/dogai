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

    # Configure the robot_state_publisher node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw, 'use_sim_time': False}] # add other parameters here if required
    )

    # Start rviz2
    node_rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', '~/ros2_ws/src/dogai/rviz/rviz_settings.rviz']
    )

    # Start joint_state_publisher
    node_joint_state_publisher = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    ld.add_action(node_rviz2)
    ld.add_action(node_robot_state_publisher)
    ld.add_action(node_joint_state_publisher)

    return ld




# # Run the node
# return LaunchDescription([
#     node_robot_state_publisher,
#     node_joint_state_publisher,
#     node_rviz2,
# ])


















# print(generate_launch_description())

"""
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_decription():
	return LaunchDescription([
		Node(
			package='',
			executable='',

		)
	])














##########################################
'''
#!/usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_decription():
	return LaunchDescription([
		Node(
			package='',
			executable='',

		)
	])

'''

"""
