from nasa_api import apod as a
from datetime import datetime
from datetime import date as dt
import tweepy as ty
import pandas as pd

# Getting API keys (not included in repo)
keys = pd.read_csv('keys.csv')

# Setting api keys
consumer_key = keys['consumer'][0]
consumer_secret_key = keys['consumer secret'][0]
access_token = keys['access'][0]
access_token_secret = keys['access secret'][0]

# Setting up Tweepy
auth=ty.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=ty.API(auth)

# Setting date and times when the tweet will be posted
tweet_time = "02:02"
next_tweet_date = "2022-03-27"

# Constantly running script
while True:

    # Getting current date and time
    now = datetime.now()
    current_time = str(now.strftime("%H:%M"))
    current_date = dt.today()
    current_date = current_date.strftime("%Y-%m-%d")
    
    # If its tweet time then tweet
    if (current_time == tweet_time) and (current_date > next_tweet_date):

        # Getting nasa info
        nasa_list = a()

        # Setting up tweet
        tweet_text = nasa_list[0] + "\n\n" + nasa_list[1] + "\n\n" + nasa_list[3] + "\n\nCredit: " + nasa_list[4]

        # Try catch block used to make sure the bot keeps running even when nasa has duplicate
        # outpus
        try:
            # Tweeting
            api.update_status(tweet_text)
        except:
            print("Duplicate Status")
        
        # Updating day after tweet
        next_tweet_date = current_date
        
    