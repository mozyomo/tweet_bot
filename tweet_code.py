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
body_list = ["蕗の薹chang!!","(^q^)イヒwwwwwwww","ﾀﾞｧｼｴﾘｲｪｽ!!（ドアが閉まります）","ついったぁの男のひと全員にマシュマロあたっく～～₍₍ ( ๑॔˃̶◡ ˂̶๑॓)◞♡♡はい、調子乗ってマシュマロあたっくしてくるやろ お前ほんまに覚えとけよ ガチで仕返ししたるからな ほんまにキレタ 絶対許さん お前のID控えたからな♡♡( ु•⌄• )","╰U╯☜(｡◐ω◐｡)ちんちん.","(☝ ՞ਊ ՞）☝(☝ ՞ਊ ՞）☝＜あ”あ”あ”あ”あ”あ”あ”あ”あ”あ”あ”あ”あ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”ぁ”","傲慢( ◠‿◠ )　ふぁぼれよ\n嫉妬(╬◠‿◠ )　俺もふぁぼれよ\n憤怒(╬◠‿◠╬)　さっさとふぁぼれよ\n怠惰_ ◠‿◠ )_　RTでもいいぞ\n強欲☜( ◠‿◠ )☞　全部ふぁぼれよ\n暴食( ◠☆◠ )　おいしいぞ\n色欲(*◔ڼ◔)　ふぁぼっ","(՞ةڼ◔)わぁぁぁぁぁぁぁぁぁぁぁぁあぁぁぁぁぁぁぁぁぁぁあぁぁぁぁぁぁ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！","+\n　　　 ∧∧　 ∧∞∧　*\n*　 ヽ(՞ةڼ◔)人(՞ةڼ◔)ﾉ\n　.～（ O x.） （ 　 O)～　+\n。*　 　∪　　　　∪　\n＿人人人人人人人人人＿\n＞ 2人はマジキチ ＜\n￣Y^Y^Y^Y^Y^Y^Y^Y^Y^￣","(╮╯╭)＜キャベツです。本当なんです。信じてください。決して玉ねぎなんかじゃないｼﾞｬｶﾞ。ほんとｼﾞｬｶﾞ。信じてほしいｼﾞｬｶﾞ！！","むすんでー　(乂’ω’)\nひらいてー　ヽ(’ω’)ﾉ\n手をうってー　(’ω’ ﾉﾉ”) ﾊﾟﾝｯ\nむーすんでー　(’ω’乂)\nまたひらいて　ヽ(’ω’)ﾉ\n手をうって　(’ω’ﾉﾉ”)ﾊﾟﾝｯﾊﾟﾝｯ\nその手を…　(’ω’ )\nう、う…＼( 'ω')／ｳｵｵｵｵｱｱｱｱｱｯ!!!"]
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