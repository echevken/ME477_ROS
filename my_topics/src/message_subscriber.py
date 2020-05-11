#!/usr/bin/env python
import rospy                       #standard
from my_topics.msg import Complex  #custom message type

def callback(msg):                     #callback
	print 'Real:', msg.real            #print real part
	print 'Imaginary:', msg.imaginary  #print imaginary part
	print                              #print nothing

rospy.init_node('message_subscriber')  #initialize node

sub = rospy.Subscriber(      #register subscription
	'complex',               #topic name
	Complex,                 #type
	callback                 #callback
)

rospy.spin()      #wait for ctrl-c