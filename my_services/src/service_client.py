#!/usr/bin/env python
import rospy                            #standard
from my_services.srv import WordCount
import sys

rospy.init_node('service_client') #initialize node

rospy.wait_for_service('word_count')      #wait for registration
word_counter = rospy.ServiceProxy(        #set up proxy
	'word_count',                         #service name
	WordCount                             #type
)
words_list = [k for k in sys.argv if 'service_client.py' not in k]
words_list = [k for k in words_list if '__' not in k]    #argument formatting
words = ' '.join(words_list)      #parse arguments
word_count  = word_counter(words) #use service

print(words+'--> has '+str(word_count.count)+' words') #print to screen