from nasa_api import apod as a
from nasa_api import download_picture
from datetime import datetime
from datetime import date as dt
import tweepy as ty
import pandas as pd
import time
import os

# Getting API keys (not included in repo)
keys = pd.read_csv('keys.csv')

# Setting api keys
consumer_key = keys['consumer'][0]
consumer_secret_key = keys['consumer secret'][0]
access_token = keys['access'][0]
access_token_secret = keys['access secret'][0]

# Setting up Tweepy
client = ty.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret_key,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# v1.1 client (needed for media uploads)
auth = ty.OAuth1UserHandler(consumer_key, consumer_secret_key, access_token, access_token_secret)
api_v1 = ty.API(auth)

# Setting date and times when the tweet will be posted
tweet_time = "12:00"
next_tweet_date = "2022-03-27"

# Constantly running script
while True:

    # Getting current date and time
    now = datetime.now()
    current_time = str(now.strftime("%H:%M"))
    current_date = dt.today()
    current_date = current_date.strftime("%Y-%m-%d")
    
    # If its tweet time then tweet
    if now.hour == 12 and now.minute == 0 and current_date > next_tweet_date:

        # Getting nasa info
        nasa_list = a()

        # Setting up tweet
        tweet_text = nasa_list[0] + "\n\n" + nasa_list[1] + "\n\n" + nasa_list[2] + "\n\nCredit: " + nasa_list[4]

        # Downloads picture to local dir
        picture = download_picture(nasa_list[0], nasa_list[3])

        # Making sure we actually get a picture=
        if picture:

            # Uploading picture
            media = api_v1.media_upload(picture)
        else:
            tweet_text += "\n\n" + nasa_list[3]

        # Try catch block used to make sure the bot keeps running even when nasa has duplicate
        # outpus
        try:
            # Tweeting
            if picture:
                client.create_tweet(text=tweet_text, media_ids=[media.media_id])
                print("Successfully posted on " + current_date + " at " + current_time)
                os.remove(picture)
            else:   
                client.create_tweet(text=tweet_text)
                print("Successfully posted on " + current_date + " at " + current_time)

        except:
            print("Duplicate Status")
        
        # Updating day after tweet
        next_tweet_date = current_date

    time.sleep(55)
        
print("THE TWITTERBOT HAS CRASHED/EXITED")