#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState


def joint_states_callback(joint_states):
    # Extract the joint positions from the JointState message
    joint_positions = joint_states.position
    
    # Publish the joint positions as a Float32MultiArray on a new topic
    pub.publish(Float32MultiArray(data=joint_positions))
    rospy.loginfo(joint_positions)
    

if __name__ == '__main__':
    # Initialize a ROS node
    rospy.init_node('ros_to_arduino')
    
    # Create a subscriber to the joint_states topic
    sub = rospy.Subscriber('joint_states', JointState, joint_states_callback)
    
    # Create a publisher for the extracted joint positions
    pub = rospy.Publisher('test_a_topic', Float32MultiArray, queue_size=12)
    
    # Spin the ROS node to process incoming messages
    rospy.spin()





'''
def publish_array():
    pub = rospy.Publisher('test_a_topic', Float32MultiArray, queue_size=12)
    rospy.init_node('ros_to_arduino', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        my_array = Float32MultiArray()
        my_array.data = [1.012, 2.012, 3.012, 4.012, 5.012, 6.012, 7.012, 8.012, 9.012, 10.012, 11.012, 12.012]
        rospy.loginfo(my_array)
        pub.publish(my_array)
        rate.sleep()



if __name__ == '__main__':
    try:
        publish_array()
    except rospy.ROSInterruptException:
        pass

'''






'''

def talker():
    pub = rospy.Publisher('test_a_topic', Float32, queue_size=36)
    rospy.init_node('ros_to_arduino', anonymous=True)
    rate = rospy.Rate(1) # 10 Hz
    
    data =0

    while not rospy.is_shutdown():
        data = data + 0.5
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()
        



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

'''