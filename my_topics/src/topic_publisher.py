#!/usr/bin/env python
import rospy                     #standard
from std_msgs.msg import Int32   #standard

rospy.init_node(            #initialize node
	'topic_publisher'       #node name
)
pub = rospy.Publisher(      #register topic
	'counter',              #topic name
	Int32,                  #type
	queue_size = 5          #queue size
)
rate = rospy.Rate(2)        #rate in Hz

count = 0                   #set counter
while not rospy.is_shutdown():  #wait for ctrl-c
	pub.publish(count) #publish count
	count += 1         #increment counter
	rate.sleep()       #wait (set by rate)