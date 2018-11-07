#!/usr/bin/env python

import sys
import json

#getting input
for line in sys.stdin:
	try:
		#removing spces before and after input
		line=line.strip()
		#splitting data based on tab spaces
		data = line.split("\n")
		#parsing it as JSON data
		json_data = json.loads(data[0],strict = False)
		#sending input to reducer
		if "authors" in json_data.keys():
			for ref in json_data["authors"]:
				print ("%s\t%s\t%s" % (ref,json_data["id"],"1"))
	except:
		pass
