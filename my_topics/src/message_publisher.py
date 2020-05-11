#!/usr/bin/env python
import rospy                       #standard
from my_topics.msg import Complex  #custom message type
from random import random          #command for random numbers

rospy.init_node('message_publisher')  #initialize node

pub = rospy.Publisher(    #register topic
	'complex',            #topic name
	Complex,              #type
	queue_size = 3        #queue size
)

rate = rospy.Rate(2)      #rate in Hz

while not rospy.is_shutdown(): #wait for ctrl-c
	msg = Complex()           #declare message type
	msg.real = random()       #random assignment for real part
	msg.imaginary = random()  #random assignment for imaginary part

	pub.publish(msg)   #publish message
	rate.sleep()       #wait (set by rate)