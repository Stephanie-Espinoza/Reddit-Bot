import praw
import time
import caffeine
import datetime

caffeine.on(display=False)

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit("liberal")

sleep_count = 0
submission_titles = []

while True:
    try: 
        for i, submission in enumerate(subreddit.top(limit = 180)):
            if submission.title in submission_titles:
                print("already posted")
                pass
            else:
                reddit.subreddit('cs40_2022fall').submit(title = submission.title,url=submission.url)
                reddit.validate_on_submit = True
                submission_titles.append(submission.title)
                print(submission.title)
                print('new submission at:',datetime.datetime.now())
                print("i =" ,i)
                time.sleep(30)
    
    except praw.exceptions.RedditAPIException as e:
        for subexception in e.items:
            if subexception.error_type == "RATELIMIT":
                error_str = str(subexception)
                print (error_str)
                if 'minute' in error_str:
                    delay = error_str.split('for ')[-1].split(' minute')[0]
                    delay = int (delay) * 60.0
                else:
                    delay = error_str.split('for ')[-1].split(' second')[0]
                    delay = int (delay)
                print ('delay=', delay)
                time.sleep(delay)
                sleep_count += 1
                print ("sleep count =", sleep_count)