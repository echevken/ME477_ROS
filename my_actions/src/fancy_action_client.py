#!/usr/bin/env python
import rospy      #standard
import time		  #regular Python timing
import actionlib  #actions
from my_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback
	#generated message types

def the_feedback_cb(feedback): #callback function
	print('[Feedback] Time elapsed: %f' %
		(feedback.time_elapsed.to_sec()))
	print('[Feedback] Time remaining: %f' %
		(feedback.time_remaining.to_sec()))

rospy.init_node('timer_action_client') #node initialization
client = actionlib.SimpleActionClient( #register client
	'timer',      #action server
	TimerAction   #action message
)

client.wait_for_server() #wait for action server
goal = TimerGoal()       #goal object
goal.time_to_wait = rospy.Duration.from_sec(5.0) #set field
#server-side abort test:
#goal.time_to_wait = rospy.Duration.from_sec(500.0)

client.send_goal(goal, feedback_cb = the_feedback_cb) #set goal
#goal preemption test:
#time.sleep(3.0)
#client.cancel_goal()

client.wait_for_result() #wait for action server
#print results
print('[Result] State: %d' % (client.get_state()))
print('[Result] Status: %s' % (client.get_goal_status_text()))
if client.get_result():
	print('[Result] Time elapsed: %f' %
		(client.get_result().time_elapsed.to_sec()))
	print('[Result] Updates sent: %d' %
		(client.get_result().updates_sent))