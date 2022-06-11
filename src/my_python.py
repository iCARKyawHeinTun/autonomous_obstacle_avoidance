#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from random import choice, randint

def movebase_client():

	# the approximate positions of the cylindrical obstacles
	exclude_array = [-13, -12, -11, -10, -9, -8, -3, -2, -1, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13]
	# create an action client 
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	# wait for the server to start up
	client.wait_for_server()
	
	while not rospy.is_shutdown():
	
		# create the desired goal position and orientation
		goal=MoveBaseGoal()
		goal.target_pose.header.frame_id = "map"
		goal.target_pose.header.stamp = rospy.Time.now()
		goal.target_pose.pose.position.x =  0.1* choice([i for i in range(-16,16) if i not in exclude_array])
		goal.target_pose.pose.position.y =  0.1* choice([i for i in range(-16,16) if i not in exclude_array])
		goal.target_pose.pose.orientation.w = 0.1 * randint(0,20)
		rospy.loginfo(goal)
	
		# send the goal to the action server
		client.send_goal(goal)
		
		# wait for the server to finish performing the acion
		wait = client.wait_for_result()
		
		if not wait:
			rospy.logerr("Action server not available!")
			rospy.signal_shutdown("Action server not available!")
		else:
			rospy.loginfo("Goal Reached!!!")
		
if __name__ == '__main__':
	try:
		# initialize the rospy node
		rospy.init_node('movebase_client_py')
		result = movebase_client()
		if result:	
			rospy.loginfo("Goal execution done!")
	except rospy.ROSInterruptException:
		rospy.loginfo("Navigation test finished.")
