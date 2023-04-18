#!/usr/bin/env python3

import sys
import rospy
import tf
from tf.transformations import *
from geometry_msgs.msg import PoseStamped

srcFr=''
tarFr=''

def main(source_frame, target_frame):
    srcFr = source_frame
    tarFr = target_frame

    rospy.init_node('fk_shower')

    
    # Create a transform listener
    listener = tf.TransformListener()
    rate = rospy.Rate(10) # 1Hz

    while not rospy.is_shutdown():
        try:

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
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rospy.logerr(f"Failed to get transform from {target_frame} to {source_frame}")
            continue
        rate.sleep()




if __name__ == '__main__':
    main(sys.argv[1], # source_frame
         sys.argv[2]  # target_frame
        )
