#!/usr/bin/env python
import sys
import json

for line in sys.stdin:
	try:
		#removing space before and after each line
		line=line.strip()
		data = line.split("\n")
		#Loading data in JSON format
		json_data = json.loads(data[0],strict = False)
		#checking for the key "references" and sending to reducer program
		if "references" in json_data.keys():
			for ref in json_data["references"]:
				print ("%s\t%s" % (ref,"1"))
	except:
		pass
