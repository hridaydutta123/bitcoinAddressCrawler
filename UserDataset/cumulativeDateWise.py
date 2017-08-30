import os
from datetime import datetime

# for each csv files in directory
for name in os.listdir("."):
	# filename ends with csv
	if name[-3:] == 'csv':
		with open(name) as f:
			# DateWise create dictionary
			dateWise = {}
			sum = 0.0

			# for each line in csv file
			for lines in f:
				#[DateTime,Amount Received]
				splitLines = lines.split(",")

				# Replace Date - with ""
				splitLines[0] = splitLines[0][:10].replace("-","")

				if splitLines[0] in dateWise:
					dateWise[splitLines[0]] += float(splitLines[1])
				else:
					dateWise[splitLines[0]] = float(splitLines[1])

			for key in sorted(dateWise.iterkeys()):
				# Cumulative sum of each element
				sum += dateWise[key]
			  	dateWise[key] = sum

				print "%s,%s" % (key, dateWise[key])
			