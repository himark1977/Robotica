#! /usr/bin/env python
import rospy
from quiz02.srv import MoveInSquare, MoveInSquareRequest
import sys

rospy.init_node('client_move_in_square')
rospy.wait_for_service('/sserver_move_in_square')

move_dir_service = rospy.ServiceProxy('/sserver_move_in_square',MoveInSquare)
move_dir_object = MoveInSquareRequest()
move_dir_object.side =  10
move_dir_object.repetitions = 8
result = move_dir_service(move_dir_object)
print(result)
