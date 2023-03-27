#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan

disToObstacle = 1

def callback(msg):

	rospy.loginfo(rospy.get_caller_id()+ 'The distance to obstacle is - %s',msg.ranges[359])

	if msg.ranges[359]>disToObstacle:

	    print('in')

	    move.linear.x = .1

	    move.angular.z = .5

	if msg.ranges[359] < disToObstacle:

	    print('out')

	    move.linear.x = 0

	    move.angular.z = .5

	while not rospy.is_shutdown():

	    pub.publish(move)

	    rate.sleep()
	    
	    
rospy.init_node('topics_quiz_node')

move = Twist()

rate=rospy.Rate(2)
    
sub = rospy.Subscriber('/scan',LaserScan,callback)


pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)


rospy.spin()
