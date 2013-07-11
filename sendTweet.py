#
#Author: Abhijit Mahalunkar
#

#!/usr/bin/python

from urllib import quote
import os
import time
import json
import random
import base64
import hmac
import binascii
import hashlib


def do_tweet(curl_request):
	os.system(curl_request)

	#data = os.popen(curl_request).read()
	#Store the response "data" in any file

def getTokens():
	f = open("tokens/token.json","r")
	tokens = json.load(f)
	consumerKey = tokens['tokens']['consumerKey']
	consumerSecret = tokens['tokens']['consumerSecret']
	oauthToken = tokens['tokens']['oauthToken']
	oauthTokenSecret = tokens['tokens']['oauthTokenSecret']
	return [consumerKey, consumerSecret, oauthToken, oauthTokenSecret]


def getTimeStamp():
	t = time.time()
	return str(int(t))


def getOauthNonce(timeStamp):
	f = open("tokens/nonce.json","r")
	nonce = json.load(f)
	f.close()

	nonce_val = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(42))

	line = "{'timeStamp': '" + str(timeStamp) + "', 'oauth_nonce': '" + str(nonce_val) + "'}"
	nonce['nonce'].append(line)

	with open('tokens/nonce.json', 'w') as outfile:
  		json.dump(nonce, outfile)

	return nonce_val


def buildAuthorizationHeader(consumerKey,oauthNonce,oauthSignature,oauthMethod,oauthTimestamp,oauthToken,oauthVersion):
	head = "'Authorization: OAuth oauth_consumer_key=" + '"' + consumerKey + '"' + ", oauth_nonce="  + '"' + oauthNonce + '"' + ", oauth_signature="  + '"' + oauthSignature  + '"' +  ", oauth_signature_method="  + '"' + oauthMethod  + '"' + ", oauth_timestamp=" + '"' + oauthTimestamp + '"' + ", oauth_token=" + '"' + oauthToken + '"' + ", oauth_version=" + '"' + oauthVersion + '"' + "'"
	return head
	

def generate_signature(signing_key, signature_base_string):
    	hashed = hmac.new(signing_key, signature_base_string, hashlib.sha1)
    	sig = binascii.b2a_base64(hashed.digest())[:-1]
    	return quote(sig, safe='~')


def collectUrlAndMethod():
    	method = "POST"
    	url = "https://api.twitter.com/1.1/statuses/update.json"

	return [method, url]


def escape(s):
	return quote(s, safe='~')


def collectParameters(consumerKey, oauthNonce, oauthToken, timeStamp, version, method, msg):
	temp = ""
	temp += "oauth_consumer_key=" + escape(consumerKey)
	temp += "&"
	temp += "oauth_nonce=" + escape(oauthNonce)
	temp += "&"
	temp += "oauth_signature_method=" + escape(method)
	temp += "&"
	temp += "oauth_timestamp=" + escape(timeStamp)
	temp += "&"
	temp += "oauth_token=" + escape(oauthToken)
	temp += "&"
	temp += "oauth_version=" + escape(version)
	temp += "&"
	temp += "status=" + escape(msg)
	
	return temp


def createSignatureBaseString(method, url, params):
	string = ""
	string = method + "&" + escape(url) + "&" + escape(params)
	return string


def getSigningKey(consumerSecret, oauthSecret):
	return consumerSecret + "&" + oauthSecret



def getCurlRequest(url, method, data, header, verbose):
	temp = ""
	temp += "curl --request '"
	temp += method
	temp += "' '"
	temp += url
	temp += "' --data '"
	temp += data
	temp += "'"
	temp += " --header "
	temp += header
	
	if(verbose == True):
		temp += " --verbose"	

	return temp


def authenticationAndSigning(msg):

	[consumer_key, consumer_secret, oauth_token, oauth_token_secret] = getTokens()
	timeStamp = getTimeStamp()
	oauth_nonce = getOauthNonce(timeStamp)
	[method, url] = collectUrlAndMethod()

	params = collectParameters(consumer_key, oauth_nonce, oauth_token, timeStamp, "1.0", "HMAC-SHA1", msg)
	signatureBaseString = createSignatureBaseString(method, url, params)
	signingKey = getSigningKey(consumer_secret, oauth_token_secret)
	
	oauth_signature = generate_signature(signingKey,signatureBaseString)

	authorizationHeader = buildAuthorizationHeader(consumer_key,oauth_nonce,oauth_signature,"HMAC-SHA1",timeStamp,oauth_token,"1.0")

	data = "status=" + escape(msg)
	curl_request = getCurlRequest(url, method, data, authorizationHeader, False)

	return curl_request


def main():

	msg = "This is the first automated tweet...!!!"

	curl_request = authenticationAndSigning(msg)
	do_tweet(curl_request)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Ctrl-C pressed"
