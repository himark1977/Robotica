#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/r2d2_diff_drive_controller/cmd_vel', Twist,queue_size=1)

rate = rospy.Rate(2)
count = Twist()
count.angular.z = 10

while not rospy.is_shutdown():
    pub.publish(count)
    rate.sleep()
