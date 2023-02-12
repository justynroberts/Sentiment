# Copyright (c) 2023 Justyn Roberts

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from textblob import TextBlob
import tweepy
import requests

# Grab Parameters from CLI
MONITOR = os.environ['MONITOR']
PD_ROUTING_KEY = os.environ['PD_ROUTING_KEY']
TW_CONSUMER_KEY =  os.environ['TW_CONSUMER_KEY']
TW_CONSUMER_SECRET =  os.environ['TW_CONSUMER_SECRET']
TW_ACCESS_TOKEN =  os.environ['TW_ACCESS_TOKEN']
TW_ACCESS_SECRET =  os.environ['TW_ACCESS_SECRET']
TW_BEARER_TOKEN =  os.environ['TW_BEARER_TOKEN']
TW_TIMEFRAME =  os.environ['TW_TIMEFRAME']
#Twitter Authentication
auth = tweepy.OAuth1UserHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
api = tweepy.API(auth)
term = MONITOR
#PagerDuty Send Event. Could use official PDPyras,but really only requires a basic post

def sendevent (tweet,sentiment,tweetid):

  
    url = "https://events.pagerduty.com/v2/enqueue"
    payload = {
    "payload": {
        "summary": "🟥 Social Media Sentiment Issue "+ tweet,
        "severity": "warning",
        "source": "Twitter-Sentiment",
    }, "custom_details": {
            "Full Message": tweet,
            "Weighting": sentiment
        },
    "routing_key": PD_ROUTING_KEY,
    "event_action": "trigger",
}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers)


# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):
    # This function gets called when the stream is working
    def on_connect(self):
        print("🤖 Connected to Twitter Stream for "+ MONITOR )
    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):
        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            analysis = TextBlob(tweet.text)
            value = str(analysis.sentiment.polarity)

            if analysis.sentiment.polarity > 0:
                print("🟩 "+ value+" " + tweet.text)
            elif analysis.sentiment.polarity == 0:
                print("🟨 "+ value+" "  + tweet.text)
            else:   
                print("🟥 "+ value+" " + tweet.text)
                print(tweet.id)
                sendevent(tweet.text,str(value),tweet.id)

            # Delay between tweets
# Creating Stream object
stream = MyStream(bearer_token=TW_BEARER_TOKEN)
rules = stream.get_rules()
for rule in rules:
    try:
        for item in rule:
            try:
                print (item.id)
                stream.delete_rules(item.id)
            except:
                a=1
    except:
        a=1
stream.add_rules(tweepy.StreamRule(term))
# Starting stream
stream.filter(tweet_fields=["referenced_tweets"])