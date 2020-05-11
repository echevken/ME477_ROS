#!/usr/bin/env python
import rospy                    #standard
from std_msgs.msg import Int32  #standard

def callback(msg):        #callback
	print(msg.data)       #print to screen

rospy.init_node('topic_subscriber') #initialize node

sub = rospy.Subscriber( #register subscription
	'counter',          #topic name
	Int32,              #type
	callback            #callback
)

rospy.spin() #wait for ctrl-c