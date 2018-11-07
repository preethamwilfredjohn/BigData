#!/usr/bin/env python

#sort with pId and author using the command -Dstream.num.map.output.key.fields=2
import sys

#Reading input from the input files
for line in sys.stdin:
	#initializing variables
	author = "-1"
	pId = "-1"		
	count = "-1"
	#removing white spaces
	line=line.strip()
	#split based on tab spaces
	data = line.split("\t")
	#differentiating based on the input
	if len(data) == 3:
		author = data[0]
		pId = data[1]
	else:
		pId = data[0]
		count = data[1]
	#sending input to the reducer code
	print("%s\t%s\t%s"%(pId,author,count))
