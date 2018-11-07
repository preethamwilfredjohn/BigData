#!/usr/bin/env python

import sys
import operator

rId = None
rAuthor = None
authorDict = {}
ct = 0
# input comes from stdin
for line in sys.stdin:
	line = line.strip()
	#parse the input we got from mapper function
	pId,author,count = line.split('\t')
	count = int(count)
	#clubbing authors based on paper Id
	if rId == pId:
		rAuthor = author
		authorDict[rAuthor] = pId
		
	else:
		if author == "-1" and count != -1:
			if rId:	
				for k,v in authorDict.items():					
					print ("%s\t%s\t%s"%(k,v,ct))				
			ct = count		
			authorDict = {}
			rId = pId		
#printing the last author
if rId:	
	for k,v in authorDict.items():
		print ("%s\t%s\t%s"%(k,v,ct))
