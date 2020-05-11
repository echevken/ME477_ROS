#!/usr/bin/env python
import rospy                      #standard
from my_services.srv import WordCount, WordCountResponse

def count_words(request):                #count_words
	return len(request.words.split())    #number of words

rospy.init_node('service_server') #initialize node

service = rospy.Service(    #register service
	'word_count',           #service name
	WordCount,              #type
	count_words             #function
)

rospy.spin()           #wait for ctrl-c