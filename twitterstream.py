import oauth2 as oauth
import urllib2 as urllib

# File to get stream of tweets to use for other projects in this folder

access_token_key = "1421848770-7AkGeKc4RpmaMF0u4JWEFox9tyRwFOki0CIUCm9"
access_token_secret = "7svI5a4vog7Ov1UgzSASylfcjjrtIPovNmqJ0wJQ"
 
consumer_key = "PMXAhOoOmKJQgZVytxZEQA"
consumer_secret = "92GQY0eJs2R9ej11mWTg7CzjQyXTM5Zp2Jro4eeeUI"


_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://api.twitter.com/1.1/search/tweets.json?q=%40obama%20%40anywhere"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
