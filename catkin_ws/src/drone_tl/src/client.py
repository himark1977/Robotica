#!/usr/bin/env python

import rospy
import actionlib
from drone_tl.msg import droneAction, droneGoal, droneResult, droneFeedback
from std_msgs.msg import Empty

class DroneActionClient(object):
    def __init__(self):
        self.client = actionlib.SimpleActionClient('drone_action', droneAction) 
        self.client.wait_for_server()

    def move_up_down(self, command):
        goal = droneGoal(command=command)
        self.client.send_goal(goal)
        self.client.wait_for_result()
        return 0
    
if __name__ == '__main__':
    rospy.init_node('drone_action_client')
    client = DroneActionClient()
    client.move_up_down("TAKEOFF")
    rospy.sleep(5)
    client.move_up_down('LAND')
    rospy.spin()
