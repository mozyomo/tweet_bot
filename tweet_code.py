#coding: utf-8
import config
import random
from requests_oauthlib import OAuth1Session
import requests
import datetime
from tweet_text import body_text 

oauth = OAuth1Session(
    config.Consumer_API_key, 
    config.Consumer_API_secret_key, 
    config.Access_Token, 
    config.Access_Token_secret
)
url = "https://api.twitter.com/1.1/statuses/update.json"
body_list = body_text()
max_index = len(body_list) - 1
body_index =random.randint(0, max_index)
body = body_list[body_index] 

timestamp = datetime.datetime.today() + datetime.timedelta(hours=9)
timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

params = {"status" : body}
response = oauth.post(url, params = params)
if response.status_code == 200 :
    print("success")
else :
    print(f"Error{response.status_code}")