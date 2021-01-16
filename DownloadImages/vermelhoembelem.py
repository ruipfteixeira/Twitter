import os
import tweepy as tw
import wget

# Twitter Developer authentication
consumer_key= 'CONSUMER-KEY'
consumer_secret= 'CONSUMER-SECRET'
access_token= 'ACCESS-TOKEN'
access_token_secret= 'ACCESS-TOKEN-SECRET'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Determine what to search for
search_words = "#HASHTAG-TO-SEARCH-FOR"
date_since = "STARTING-DATE"

# Collect tweets and filter retweets
new_search = search_words + " -filter:retweets"

tweets = tw.Cursor(api.search,
                       q=new_search,
                       include_entities=True,
                       since=date_since).items()

def get_tweet_url(tweet):
    tweet_id = tweet.id_str
    screen_name = tweet.user.screen_name

    tweet_url = "https://twitter.com/{screen_name}/status/{tweet_id}"
    tweet_url = tweet_url.format(screen_name=screen_name,tweet_id=tweet_id)

    return tweet_url

# Download the images
path = 'FOLDER-FOR-DOWNLOAD'
for tweet in tweets:
    if 'media' in tweet.entities:
        for media in tweet.extended_entities['media']:
            wget.download(media['media_url'],path)
