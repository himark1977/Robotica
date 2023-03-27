#!  /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print(msg.pose.pose.position.x)

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/r2d2_diff_drive_controller/odom',Odometry,callback)

rospy.spin()
