# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '747568332866359297-FtmQEr8fEjB2JKphZDw5RyzdnI656Tm'
ACCESS_SECRET = 'zZKeiumxH3CVEDFdUpyR6fX4CWbb98qTDA2Fv8tFGfl0k'
CONSUMER_KEY = 'EVtN9eDkee4wAsZ35cR0WYj8F'
CONSUMER_SECRET = 'DYnEsBbuGjgDDUHNmoqNxQ7gj3a4ts1pLJEaPRDy95WjeCYzpd'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="pikachu", language="en")

#nj_trends = twitter.trends.place(_id = 2459115)
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 

#print json.dumps(nj_trends,indent=4)
