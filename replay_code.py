#coding: utf-8
import csv
import config
import random
from requests_oauthlib import OAuth1Session
import requests
import datetime
import json
import pandas as pd
import sys
from tweet_text import reply_text

oauth = OAuth1Session(
    config.Consumer_API_key, 
    config.Consumer_API_secret_key, 
    config.Access_Token, 
    config.Access_Token_secret
)
#リプライ情報の取得
url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=8"
response = oauth.get(url)
if response.status_code == 200 :
    print("Success")
    response_json = response.json() #APIで取得したJSONファイルの読み込み。データはリストなので、長さを取得して繰り返し処理
    list_len = len(response_json) 
    id_list = []                    #今回の処理でリプを飛ばす返信先を格納するリスト
    replay_adress_list = []         #@マーク抜きのアカウント名を格納するリスト
    with open("log.csv") as f :
        reader = csv.reader(f)
        lists = [row for row in reader]
        if [""] in lists :
            lists.remove([""])
        elif ['', '0'] in lists :
            lists.remove(['', '0'])
    print(lists)
    if lists == []:
        old_id_list = lists
    else :
        old_id_list = []
        for g in range(len(lists)):
            old_id_list.append(lists[g][1])
    for i in range(list_len) :
        tweet_id = response_json[i]["id"]
        if not str(tweet_id) in old_id_list :
            id_list.append(tweet_id)
            old_id_list.append(tweet_id)
            replay_adress_list.append(response_json[i]["user"]["screen_name"])
    df = pd.DataFrame(old_id_list)
    df.to_csv("log.csv", mode = "w")
    if not replay_adress_list == []:
        for k in replay_adress_list :
            adress_name = "@" + k
            print(adress_name)

    #返信内容の決定,返信内容には必ずadress_nameを入れること
    url = "https://api.twitter.com/1.1/statuses/update.json"
    body_list = reply_text(adress_name)
    max_index = len(body_list) - 1
    body_index =random.randint(0, max_index)
    body = body_list[body_index] 
    params = {"status" : body}
    response = oauth.post(url, params = params)
    if response.status_code == 200 :
        print("success")

    else :
        print(f"Error{response.status_code}")