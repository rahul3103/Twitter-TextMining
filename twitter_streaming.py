#Import important methods from tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Definig variables for Twitter Credentials

access_token = "aTOz"
access_token_secret = "atoz"
consumer_key = "atoz"
consumer_secret = "atoz"

#StdOut received tweets

class StdOutListener(StreamListener):

	def on_data(self,data):
		print data
		return True

	def on_error(self,status):
		print status

if __name__ == '__main__':

	#Twitter authentication and connection

	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	#Filter Twitter Streams by Keywords
	stream.filter(track=['cricket','football','tennis'])