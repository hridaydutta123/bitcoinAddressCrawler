import pymongo
import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("localhost", 27017, maxPoolSize=50)

# Connect to db tweets
db=client.bitcoindb

# Collection - users
collection=db['users']

cursor = collection.find({})

for documents in cursor:
	profileID = documents['profileID']
	print "************" + str(profileID) + "************" 
	for transactions in documents['data']['txs']:
		dest = transactions['out'][0]['addr']
		source = transactions['inputs'][0]['prev_out']['addr']
		amount = transactions['out'][0]['value']/100000000
		datetime = transactions['time']

		# Check if destination is profile ID
		if dest == profileID:
			print source,dest,amount,datetime