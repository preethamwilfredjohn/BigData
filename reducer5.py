#!/usr/bin/env python

import sys
import operator

current_Id = None
current_count = 0
Id = None
moreRef={}
# input comes from stdin which is an output of mapper function
for line in sys.stdin:
	try:
		#remove the spaces before and after each line of input
		line = line.strip()
		#parse the input we got from mapper function
		Id,count = line.split('\t',1)
		count = int(count)
		#logic for reducing 
		if current_Id == Id:
			current_count += count
		else:
			if current_Id:
					#storing the result in a dictionary
					moreRef[current_Id] = current_count 
			current_count = count
			current_Id = Id
			
	except:
		pass
#sorting the dictionary
sorteddict = sorted(moreRef.items(), key = lambda kv : kv[1], reverse = True)
#printing the top 5 referenced paper
for x in sorteddict[:5]:
	print x

