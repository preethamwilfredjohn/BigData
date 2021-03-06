#!/usr/bin/env python

import sys

current_Id = None
current_count = 0
Id = None
maxCount = None
moreRef = {}
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
				#checking for the authors with more published paper
				print ("%s\t%s"% (current_Id,current_count))
			current_count = count
			current_Id = Id
			
	except:
		pass	
#checking for last record
if current_Id:
	#checking for the authors with more published paper
	print ("%s\t%s"% (current_Id,current_count))