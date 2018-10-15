#!/usr/bin/env python
import sys
import json

#gets data from the standard input which reads from file
for line in sys.stdin:
	try:
		#remove the spaces before and after each line of input
		line=line.strip()
		#load json data
		json_data = json.loads(line[0],strict = False)
		#look for authors key 
		if "authors" in json_data.keys():
			#print the dataset to reducer program
			for ref in json_data["authors"]:
				print ("%s\t%s" % (ref,"1"))
	except:
		pass
