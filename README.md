# tweet_bot
## about
tweet_bot is a Twitter BOT. You can send automatic tweets and replies to your friends with predefined contents.
To use it, you need to use PaaS like Heroku or Windows Task Scheduler.

## config.py
This is a location of the Twitter_API_key.
You must get the API from Twitter Developer and store it in this file.

## index.py
A dummy web app to keep processes running on Heroku. The content is sample code of the lightweight web framework bottle.

## tweet_code.py
This is the body of Tweets BOT, where body_list contains the content you want to tweet.

## replay_code.py
The body of the automatic reply BOT, put the content you want to reply to in body_list. Don't forget to put "address_namde" in the body_list.

## log.csv
A place to store and store the IDs of comments that have been skipped in the past.
