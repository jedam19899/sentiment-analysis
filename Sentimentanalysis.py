import tweepy 
from textblob import textblob

consumer_key = "hBp5aFNjr6gnToiVyTfbYfNhR"
consumer_secret = "x1mJWuuaZDqtaB30ehF2TE7jO5lW1PfqNoaTuKNDE1iAWcOU4c"

access_token = "1008774831393984513-RAsL0rP3FJKmEng0UlHF7MUi3QFRrv"
access_token_secret = "SgR1S02EpGZ0mRMrXkojmniwFFUmbqCX3IF9pM1zfP1kb"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)