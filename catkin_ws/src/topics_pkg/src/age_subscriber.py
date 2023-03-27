#!  /usr/bin/env python
import rospy
from topics_pkg.msg import Age

def callback(msg):
    print(msg)

rospy.init_node('age_subscriber')
sub = rospy.Subscriber('/Age',Age,callback)

rospy.spin()
