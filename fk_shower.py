#!/usr/bin/env python3

import sys
import rospy
import tf
from tf.transformations import *
from geometry_msgs.msg import PoseStamped

srcFr=''
tarFr=''

'''
def callback(msg):
    # rospy.loginfo(msg.pose.position)
    pos  = str(msg)
    rospy.loginfo(pos)
    # quat = msg.pose.orientation
    # print(f"Received transformation: translation ({pos.x}, {pos.y}, {pos.z}), rotation ({quat.x}, {quat.y}, {quat.z}, {quat.w})")


    # (trans, rot) = msg
    # Combine rotation matrix and translation vector 
    # transform_matrix = quaternion_matrix(rot)
    # transform_matrix[0][3] = trans[0]
    # transform_matrix[1][3] = trans[1]
    # transform_matrix[2][3] = trans[2]
    # rospy.loginfo(f"\n rotation (in quaternions): \t{rot}\n Translation: \t\t\t{trans}\nTransformation matrix:\n{transform_matrix}") # Print transformation matrix


def main(source_frame, target_frame):
    srcFr = source_frame
    tarFr = target_frame

    rospy.init_node('tf_listener')
    
    # Create a transform listener
    listener = tf.TransformListener()

    rate = rospy.Rate(1.0) # 1Hz


    # Wait for the transformation to become available
    listener.waitForTransform(source_frame, target_frame, rospy.Time(), rospy.Duration(1.0))

    # Subscribe to the transformation topic
    rospy.Subscriber('/tf', PoseStamped, callback)

    # Spin the node
    rospy.spin()


'''
def main(source_frame, target_frame):
    srcFr = source_frame
    tarFr = target_frame

    rospy.init_node('fk_shower')

    
    # Create a transform listener
    listener = tf.TransformListener()
    rate = rospy.Rate(10) # 1Hz

    while not rospy.is_shutdown():
        try:

            # listener.waitForTransform(tarFr, srcFr, rospy.Time(), rospy.Duration(1))
            (trans, rot) = listener.lookupTransform(f"/{srcFr}", f"/{tarFr}", rospy.Time(0))
            # Combine rotation matrix and translation vector 
            transform_matrix = quaternion_matrix(rot)
            transform_matrix[0][3] = trans[0]
            transform_matrix[1][3] = trans[1]
            transform_matrix[2][3] = trans[2]

            rot_eul = euler_from_quaternion(rot)
            rospy.loginfo(f"""\n
- Translation:                  {trans}
- rotation (in quaternions):    {rot}
- rotation (euler):             {rot_eul}
- Transformation matrix:
{transform_matrix}
-------------------------------------------""")
            # Print transformation matrix
            # Subscribe to the transformation topic
            # rospy.Subscriber('/tf', PoseStamped, callback)
            # rospy.spin()
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rospy.logerr(f"Failed to get transform from {target_frame} to {source_frame}")
            continue
        rate.sleep()




if __name__ == '__main__':
    main(sys.argv[1], # source_frame
         sys.argv[2]  # target_frame
        )
