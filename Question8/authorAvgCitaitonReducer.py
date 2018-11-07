#!/usr/bin/env python
import sys

current_author = None
current_count = 0
finalDict = {}

for line in sys.stdin:
	line = line.strip()
	author,count = line.split("\t")
	count = int(count)
	#calculation for authors most cited paper
	if current_author == author:
		tempList.append(count)
	else:
		if current_author:
			#calculation of the average
			avgCitationList = (sorted(tempList,reverse = True)[:3])
			summation = 0.0
			for i in avgCitationList:
				summation = summation + i	
			avgCitation = summation/3			
			finalDict[current_author] = avgCitation		
		#creating list to append count of each paper citation to author		
		if current_author != author:
			tempList = []
		tempList.append(count)
		current_author = author

#for last value in the dictionary
if current_author:
	avgCitationList = (sorted(tempList,reverse = True)[:3])
	summation = 0.0
	for i in avgCitationList:
		#print type(i)
		summation = summation + i	
		avgCitation = summation/3			
		finalDict[current_author] = avgCitation

#sorting and printing the output
sorteddict = sorted(finalDict.items(), key = lambda kv : kv[1], reverse = True)
for x in sorteddict[:10]:
	print x
