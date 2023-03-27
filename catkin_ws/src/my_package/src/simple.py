#!/usr/bin/env python
import rospy
rospy.init_node("Friends")
rate = rospy.Rate(2)
while not rospy.is_shutdown():
	print("How you doing?")
	rate.sleep()
