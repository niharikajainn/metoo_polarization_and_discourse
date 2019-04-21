import json
from pprint import pprint
import requests
import re
import pickle
import time

next = "[initial_next_token]"

headers = {
    'authorization': 'Bearer [your_generated_bearer_token]',
    'content-type': 'application/json',
}

data = '{"query":"#MeToo lang:en", "maxResults": "500", "fromDate": "201710050000", "toDate": "201810050000", "next": "[initial_next_token]"}'

no_next = False

for iter in range(5):
    if no_next:
        break

    for count in range(15):
        if iter == 0:
            count += 1

        #make API request
        response = requests.post('https://api.twitter.com/1.1/tweets/search/fullarchive/[your_env_name]', headers=headers, data=data)
        print(response.json())

        #each tweet is a json doc
        with open('tweets.json', 'w') as f:
            json.dump(response.json(), f)

        tweets = None
        with open('tweets.json', 'r') as data_file:
            tweets = json.loads(data_file.read())

    if "next" in tweets: #loads query with new next token
            print(tweets["next"])
            next = tweets["next"]
            r, _ = re.split(', "next"', data)
            r += ', "next": '
            r += '\"'
            r += next
            r += '\"}'
            data = r
        else:
            no_next = True

        texts = []
        text = ""
        tweet = None

        #save only text of each tweet, accounts for 280-character tweets, links, and manual retweets
        for i in range(len(tweets["results"])):
            truncated = None
            if "retweeted_status" in tweets["results"][i]:
                tweet = tweets["results"][i]["retweeted_status"]
            else:
                tweet = tweets["results"][i]
            truncated = tweet["truncated"]
            if truncated: #extended_tweet field only exists if truncated val is true
                text = tweet["extended_tweet"]["full_text"]
                texts.append(text)
            else:
                text = tweet["text"]
                texts.append(text)

        texts = [re.sub('\n', '', text) for text in texts]
        texts = [re.sub('https://t.co/[a-zA-Z0-9]{10}', "", text) for text in texts]

        #update file of tweets
        documents = []
        with open("tweets_metoo.txt", "rb") as f:
            documents = pickle.load(f)

        documents.extend(texts)

        with open("tweets_metoo.txt", "wb") as f:
            pickle.dump(documents, f)

    #only 15 requests are allowed in a 15-minute window
    time.sleep(900)
