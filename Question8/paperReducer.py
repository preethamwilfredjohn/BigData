#!/usr/bin/env python

import sys

current_Id = None
current_count = 0
Id = None

# input comes from stdin
for line in sys.stdin:
	try:
		line = line.strip()		
		#parse the input we got from mapper.py
		Id,count = line.split('\t')
		count = int(count)	
		#counting the number of similar paper
		if current_Id == Id:
				current_count += count
		else:
			if current_Id:
				print ("%s\t%s" % (current_Id,current_count)) 
			current_count = count
			current_Id = Id	
	except:
		pass
#for last row
if current_Id == Id:
	print '%s\t%s' % (current_Id, current_count)
