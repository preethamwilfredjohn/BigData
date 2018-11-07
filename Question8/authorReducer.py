#!/usr/bin/env python

import sys
import operator


Id = None

# input comes from stdin
for line in sys.stdin:
	try:
		line = line.strip()
		#parse the input we got from mapper.py
		author,Id,count = line.split('\t')
		count = int(count)
		#printing output
		print("%s\t%s\t%s" % (author,Id,count))
	except:
		pass

