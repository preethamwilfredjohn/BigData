#!/usr/bin/env python

import sys
import json

#Reading input from the input files
for line in sys.stdin:
	#removing white spaces
	line=line.strip()
	#split based on tab spaces
	author,pId,count = line.split("\t")
	#sending input to the reducer code
	print("%s\t%s"%(author,count))
