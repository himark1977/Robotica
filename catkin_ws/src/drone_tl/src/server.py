#!/usr/bin/env python

import rospy
import actionlib
from drone_tl.msg import droneAction, droneGoal, droneResult, droneFeedback
from std_msgs.msg import Empty

class DroneActionServer(object):
    def __init__(self):
        self._as = actionlib.SimpleActionServer('drone_action', droneAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()
        self._pub = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=10)
        self._pub2 = rospy.Publisher('/ardrone/land', Empty, queue_size=10)
        self._rate = rospy.Rate(1)
        self._feedback = droneFeedback()
        self._result = droneResult()

    def execute_cb(self, goal):
        if goal.command == 'TAKEOFF':
            self._pub.publish(Empty())
            self._feedback.feedback = 'Taking off...'
            self._as.publish_feedback(self._feedback)
            self._rate.sleep()
            self._result.result = ''
            self._as.set_succeeded(self._result)
        elif goal.command == 'LAND':
            self._pub2.publish(Empty())
            self._feedback.feedback = 'Landing...'
            self._as.publish_feedback(self._feedback)
            self._rate.sleep()
            self._result.result = ''
            self._as.set_succeeded(self._result)
        success = True

if __name__ == '__main__':
    rospy.init_node('drone_action_server')
    server = DroneActionServer()
    rospy.spin()
    


