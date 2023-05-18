#!/usr/bin/env python3



import rospy
from std_msgs.msg import Float32

from sensor_msgs.msg import JointState



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

