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




The file build.sh can be used to build and run a local docker image
`cd` to src directory

    docker build -t sentiment .
   
    
## Docker Parameters
To run the container, you will need to create a file with a set of configuration items, with an example below:

    docker run -d --name sentiment /
    MONITOR="Hashtag or Twitter Handle eg @Justynroberts" /
    PD_API_KEY="Enter your PagerDuty API Key"/
    TW_CONSUMER_KEY="Twitter Consumer Key" /
    TW_CONSUMER_SECRET="Twitter Consumer Secret" /
    TW_ACCESS_TOKEN="Twitter Access Token" /
    TW_ACCESS_SECRET="Twitter Access Secret" /
    TW_BEARER_TOKEN="This is the fourth environment variable" /
    TW_TIMEFRAME="100" /
    sentiment
    
## Caveats
This isnt particularly robust, or configurable.. Currently `Proof Of Concept.`
But it works.
