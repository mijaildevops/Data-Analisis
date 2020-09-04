import tweepy
import json
# Setting
from Settings import APIKey, APISecret, AccessSecret, AccessToken
# GUID
import uuid
#date
import datetime

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
Guid = str(IdUnico)

#///////////////////////////////////////////
#Search Parameter
#///////////////////////////////////////////
SearchParameter = "BancoPichincha"


# Setting Autentificaion
consumer_key = APIKey
consumer_secret = APISecret
access_token = AccessToken
access_token_secret = AccessSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

# data user Me
#data = api.me()
#print (json.dumps(data._json, indent=2))

# Get data User
#data = api.get_user("@NetlifeEcuador")
#print (json.dumps(data._json, indent=2))

# Buscar Tweets
for tweet in tweepy.Cursor(api.search, q=SearchParameter, 
tweet_modes="extended").items(10000):
    #print (json.dumps(tweet._json, indent=2)) # all text
    # fetching the full_text attribute 
    idtweet = tweet.id 
    createdtweet = tweet.created_at 
    usertweet = tweet.user.name 
    TweetMsg = tweet.text 
    retweeted = tweet.retweeted 
    retweet_count =tweet.retweet_count 
    lang = tweet.lang 

    # HoraLocal Ecuador
    # date Local
    DateLocalTweet = createdtweet - datetime.timedelta(hours=5)
     
    
    print ('id : ', idtweet )
    print ('createdUTC  : ', createdtweet)
    print ('DateLocal: ', DateLocalTweet)
    print ('user : ', usertweet)
    print ('Tweet: ', TweetMsg)
    print ('retweeted : ', retweeted )
    print ('retweet_count : ',retweet_count )
    print ('lang  : ', lang  )
    
    # save Resultado        
    """ from SaveTweet import OldTweet
    OldTweet (Guid, createdtweet, DateLocalTweet, idtweet, usertweet, TweetMsg, SearchParameter, retweeted, retweet_count, lang)
     """

