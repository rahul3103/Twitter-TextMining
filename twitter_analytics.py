import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from Tkinter import *

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
tweets = pd.DataFrame()

#adding columns

tweets['text'] = map(lambda tweet:tweet['text'] if tweet['text'] else '', tweets_data)

#tweets['text'] = [tweet['text'] for tweet in tweets_data]

tweets['lang'] = map(lambda tweet:tweet['lang'] if tweet['lang'] else '', tweets_data)

#tweets['lang'] = [tweet['lang'] for tweet in tweets_data]

tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

#Adding Charts
tweets_by_lang = tweets['lang'].value_counts()

#pd.value_counts(tweets.values.flatten())

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')