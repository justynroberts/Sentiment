# Sentimental

  Social Media Sentiment Analysis.

>   Because social media streams can need human response

## About
Combination of 

 - Twitter Streams 
 - Sentiment Analysis 
 - PagerDuty

Potential of adding additional Social Media Streams, Tweaking Sensitivity will come in the future.

## Deployment
Preferred deployment via Docker or ECS.

Clone the repository with 

    git clone https://github.com/justynroberts/sentimental.git .

To get the latest repo

**Build & Run**

    cd sentimental

To clean any previous builds

    docker rm -f sentiment

The file example build.sh can be used to build and run a local docker image
`cd` to src directory

    docker build -t sentiment .
   
## Docker Parameters
To run the container, you will need to execute the parameter with a set of configuration items, with an example below:

    docker run -e MONITOR="@twitterhandle" -e PD_ROUTING_KEY="PagerDuty Routing Key" -e TW_CONSUMER_KEY="Twitter Consumer Key" -e TW_CONSUMER_SECRET="Twitter Consumer Secret" -e TW_ACCESS_TOKEN="Twitter Access Token" -e TW_ACCESS_SECRET="Twitter Access Token" -e TW_BEARER_TOKEN="Twitter Bearer Token" -e TW_TIMEFRAME="100" -d --name sentiment sentiment

**Parameters** 
Broken down as:

MONITOR="Hashtag or Twitter Handle eg @Justynroberts"

PD_ROUTING_KEY="Enter your PagerDuty Service Routing Key"

TW_CONSUMER_KEY="Twitter Consumer Key"

TW_CONSUMER_SECRET="Twitter Consumer Secret"

TW_ACCESS_TOKEN="Twitter Access Token"

TW_ACCESS_SECRET="Twitter Access Secret"

TW_BEARER_TOKEN="Twitter Bearer Token"

TW_TIMEFRAME="100" # Time window in seconds for repeat tweet before notification

**Logs**

To grab inflight logs

    docker logs sentiment -f
 
 ## Twitter
  You WILL need a set of API tokens/secrets from developer.twitter.com
  
## Caveats
This isnt particularly error robust, or configurable.. Currently `Proof Of Concept.`
But it works.
