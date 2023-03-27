#! /usr/bin/env python

import rospy
from topics_pkg.msg import Age

rospy.init_node('Age_publisher')
pub = rospy.Publisher('/Age',Age,queue_size=1)
rate=rospy.Rate(2)
count=Age()
count.years = 2023
count.month = 69
count.days = 420

while not rospy.is_shutdown():
	pub.publish(count)
	rate.sleep()