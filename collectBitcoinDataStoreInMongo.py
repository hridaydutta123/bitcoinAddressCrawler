import urllib
import json
from pymongo import MongoClient
import pymongo
from bson import ObjectId

profileLinks = ['https://blockchain.info/address/115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn', 'https://blockchain.info/address/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94', 'https://blockchain.info/address/12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw']

# Connect to MongoDB
client = MongoClient("localhost", 27017, maxPoolSize=50)

# Connect to db bitcoindb
db=client.bitcoindb


for profiles in profileLinks:
	offset = 0
	while offset < 101:
		fullUrl = profiles + '?format=json&offset=' + str(offset) + '&filter=2'
		response = urllib.urlopen(fullUrl)
		data = json.loads(response.read())
		if offset > 0:
			matchedUser = db.wannacry.find_one({'profileID': profiles[32:]})
			txsData = []
			print matchedUser['_id']
			txsData.append(data['txs'])
			print data['txs']

			db.wannacry.update({'_id': ObjectId(matchedUser['_id'])}, {'$push': {'data': {'txs':{data['txs']}}}})
		else:
			result = db.wannacry.insert_one(
				{	
					"profileID" : profiles[32:],
					"data" : data
				}
			)
		offset = offset + 50
