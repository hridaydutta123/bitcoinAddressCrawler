import re, urlparse, httplib, urllib2, pickle

addresses = ['13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94','12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw','115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn']

content = []

def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url

with open('actual_ransom_tweets.csv') as f:
    for lines in f:
    	content.append(lines)

finalUrlList = []
for line in content:
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
	if urls:
		finalUrl = unshorten_url(urls[0])
		#print str(urls[0]) + "->" + str(finalUrl)
		if finalUrl.startswith('https://blockchain.info/address/'):
			finalUrlList.append(finalUrl)

expandedUrlFile = open('expandedUrlList.txt', 'w')
for item in finalUrlList:
  expandedUrlFile.write("%s\n" % item)

# Found the bitcoin received list in finalUrlList
#for blockchainUrls in finalUrlList:

content = urllib2.urlopen(finalUrlList[0]).read()
print content


