#!/usr/bin/env python
import rospy      #standard
import time		  #regular Python timing
import actionlib  #actions
from my_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback
	#generated message types

def do_timer(goal):
	start_time = time.time() #start timer
	update_count = 0
	if goal.time_to_wait.to_sec() > 60.0: #duration capped at 60.0s
		result = TimerResult() #create result object
		result.time_elapsed = rospy.Duration.from_sec(
			time.time() - start_time) #set results
		result.updates_sent = update_count
		server.set_aborted(result, "Abort: too long to wait")
		return #requested wait is too long
	while (time.time() - start_time) < goal.time_to_wait.to_sec():
		#while goal duration is not met
		if server.is_preempt_requested(): #check preempted timer
			result = TimerResult()
			result.time_elapsed = rospy.Duration.from_sec(
				time.time() - start_time) #set results
			result.updates_sent = update_count
			server.set_preempted(result, "Timer preempted")
			return
		feedback = TimerFeedback() #create feedback object
		feedback.time_elapsed = rospy.Duration.from_sec(
			time.time() - start_time) #set field
		feedback.time_remaining = \
			goal.time_to_wait - feedback.time_elapsed #set field
		server.publish_feedback(feedback)
		update_count += 1
		time.sleep(1.0) #wait
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(
		time.time() - start_time)
	result.updates_sent = update_count
	server.set_succeeded(result, "Timer completed successfully")

rospy.init_node('timer_action_server')	#node initialization
server = actionlib.SimpleActionServer(
	'timer', TimerAction, do_timer, False
)
server.start()
rospy.spin() #run until ctrl-c	