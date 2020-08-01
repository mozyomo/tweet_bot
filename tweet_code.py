import config
import random
from requests_oauthlib import OAuth1Session
import requests
import datetime

oauth = OAuth1Session(
    config.Consumer_API_key, 
    config.Consumer_API_secret_key, 
    config.Access_Token, 
    config.Access_Token_secret
)
url = "https://api.twitter.com/1.1/statuses/update.json"
body_list = ["蕗の薹chang!!","(^q^)イヒwwwwwwww","ﾀﾞｧｼｴﾘｲｪｽ!!（ドアが閉まります）","ついったぁの男のひと全員にマシュマロあたっく～～₍₍ ( ๑॔˃̶◡ ˂̶๑॓)◞♡♡はい、調子乗ってマシュマロあたっくしてくるやろ お前ほんまに覚えとけよ ガチで仕返ししたるからな ほんまにキレタ 絶対許さん お前のID控えたからな♡♡( ु•⌄• )","╰U╯☜(｡◐ω◐｡)ちんちん."]
max_index = len(body_list) - 1
body_index =random.randint(0, max_index)
body = body_list[body_index] 

timestamp = datetime.datetime.today() + datetime.timedelta(hours=9)
timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

params = {"status" : body + " " + timestamp}
response = oauth.post(url, params = params)
if response.status_code == 200 :
    print("success")
else :
    print(f"Error{response.status_code}")