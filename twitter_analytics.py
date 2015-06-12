import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


def main():

	tweets_data_path = 'C:/Users/e2sn7cy/Documents/GitHub/twitter_data.txt'

	tweets_data = []

	tweets_file = open(tweets_data_path, 'r')

	for line in tweets_file:
		try:
			tweet = json.loads(line)
		except:
			continue
    		if not all([x in tweet for x in ['text', 'lang', 'place']]):
    			continue
    		if tweet['place'] and not 'country' in tweet['place']:
    			continue
    		tweets_data.append(tweet)

	#print len(tweets_data)

	#DataFrame
	#Structuring Tweets
	tweets = pd.DataFrame()

	#adding columns

	#tweets['text'] = map(lambda tweet:tweet['text'] if tweet['text'] else '', tweets_data)
	tweets['text'] = [tweet['text'] for tweet in tweets_data]
	#tweets['lang'] = map(lambda tweet:tweet['lang'] if tweet['lang'] else '', tweets_data)
	tweets['lang'] = [tweet['lang'] for tweet in tweets_data]
	tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

	#Analyzing Tweets by Language
	print 'Analyzing tweets by language\n'
	tweets_by_lang = tweets['lang'].value_counts()
	#pd.value_counts(tweets.values.flatten())
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets',fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	plt.savefig('tweet_by_lang.png', format='png')


	#Analyzing Tweets by Country
	print 'Analyzing tweets by country\n'
	tweets_by_country = tweets['country'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Countries', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
	tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
	plt.savefig('tweet_by_country.png', format='png')

	#Adding games columns to the tweets DataFrame
	print 'Adding game tags to the data\n'
	tweets['cricket'] = tweets['text'].apply(lambda tweet: word_in_text('cricket', tweet))
	tweets['football'] = tweets['text'].apply(lambda tweet: word_in_text('football', tweet))
	tweets['tennis'] = tweets['text'].apply(lambda tweet: word_in_text('tennis', tweet))

	#Analyzing Tweets by games: First attempt
	print 'Analyzing tweets by games: First attempt\n'
	games = ['cricket', 'football', 'tennis']
	tweets_by_games = [tweets['cricket'].value_counts()[True], tweets['football'].value_counts()[True], tweets['tennis'].value_counts()[True]]
	x_pos = list(range(len(games)))
	width = 0.8
	fig, ax = plt.subplots()
	plt.bar(x_pos, tweets_by_games, width, alpha=1, color='g')
	ax.set_ylabel('Number of tweets', fontsize=15)
	ax.set_title('Ranking: cricket vs. football vs. tennis (Raw data)', fontsize=10, fontweight='bold')
	ax.set_xticks([p + 0.4 * width for p in x_pos])
	ax.set_xticklabels(games)
	plt.grid()
	plt.savefig('tweet_by_games_1.png', format='png')

if __name__=='__main__':
	main()