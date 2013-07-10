from urllib import urlencode
import os
import time

def do_tweet (st):
	t = urlencode({'status':st})

	#url = "curl --request 'POST' 'https://api.twitter.com/1.1/statuses/update.json' --data '" + t + """' --header 'Authorization: OAuth oauth_consumer_key="Azt3puFmENnKPU9a3G5XQ", oauth_nonce="97539555eaded542be63195e0aa89100", oauth_signature="OZFH2T1q4mLwElx7zRX05cpyuMI%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1373426476", oauth_token="99779165-GVtlEl4H2QomTXPBXktvMNUfqvBThKJlOOTYZh0fM", oauth_version="1.0"' --verbose"""
	#os.system(url)
	#url = """curl --request 'POST' 'https://api.twitter.com/1.1/statuses/update.json' --data 'status=Maybe%20he%27ll%20finally%20find%20his%20keys.%20peterfalk' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="99048f92fa70ff414d0fdda6f23d151b", oauth_signature="gmoBoDchWzhy%2BnKDq0N%2B7MiVb%2Bs%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp=""" +'"'+ str(int(time.time())) +'"'+ """, oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose"""
	#print url
	#time.sleep(5)
	#os.system("""curl --request 'POST' 'https://api.twitter.com/1.1/statuses/update.json' --data 'status=Maybe%20he%27ll%20finally%20find%20his%20keys.%20peterfalk' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="99048f92fa70ff414d0fdda6f23d151b", oauth_signature="gmoBoDchWzhy%2BnKDq0N%2B7MiVb%2Bs%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp=""" +'"'+ str(int(time.time())) +'"'+ """, oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose""")
	#os.system("""curl --get 'https://api.twitter.com/1.1/statuses/mentions_timeline.json' --data 'count=2&since_id=14927799' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="3d9368a5a242a9c70f2c5d6a35dd0f96", oauth_signature="m99nOo5JA6rwmLbJ4DiRK9HFf94%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1373461265", oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose""")

	os.system("""curl --request 'POST' 'https://api.twitter.com/1.1/statuses/update.json' --data 'status=Maybe+he%27ll+finally+find+his+keys.+%23peterfalk' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="06dddd2c1825b942ed148c271b5d2fed", oauth_signature="NBPzcfBMD66VdFsaVyklstnVukA%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1373463959", oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose""")

	data = os.popen("""curl --get 'https://api.twitter.com/1.1/statuses/mentions_timeline.json' --data 'count=2&since_id=14927799' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="3d9368a5a242a9c70f2c5d6a35dd0f96", oauth_signature="m99nOo5JA6rwmLbJ4DiRK9HFf94%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1373461265", oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose""").read()

	f = open("resp.dat","w")
	f.write(data)
	f.close()

	url = """curl --get 'https://api.twitter.com/1.1/statuses/mentions_timeline.json' --data 'count=2&since_id=14927799' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="3d9368a5a242a9c70f2c5d6a35dd0f96", oauth_signature="m99nOo5JA6rwmLbJ4DiRK9HFf94%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1373461265", oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose"""
	#url = """curl --get 'https://api.twitter.com/1.1/statuses/mentions_timeline.json' --data 'count=2&since_id=14927799' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="3d9368a5a242a9c70f2c5d6a35dd0f96", oauth_signature="m99nOo5JA6rwmLbJ4DiRK9HFf94%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="""+'"'+ str(int(time.time())) +'"'+""", oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose"""
	#data = os.popen("""curl --get 'https://api.twitter.com/1.1/statuses/mentions_timeline.json' --data 'count=200' --header 'Authorization: OAuth oauth_consumer_key="KtBRUg8yxZOLMjsPYJiQCQ", oauth_nonce="3d9368a5a242a9c70f2c5d6a35dd0f96", oauth_signature="m99nOo5JA6rwmLbJ4DiRK9HFf94%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1373461265", oauth_token="458269836-eZOOctDi7siYRraEBO1D92qZgx9JqdxwAVRqEA", oauth_version="1.0"' --verbose""").read()
	data = os.popen(url).read()

	f = open("resp1.dat","w")
	f.write(data)
	f.close()


def getTokens():
	
def main():

	[consumer_key, oauth_token] = getTokens()
	

	do_tweet ("Hello Goodmorning...!!!")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Ctrl-C pressed"
