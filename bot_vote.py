import praw
from textblob import TextBlob
import caffeine

caffeine.on(display=False)

count = 0
reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('cs40_2022fall')

for submission in subreddit.top(limit = None):
    submission.comments.replace_more(limit = None)
    print(submission.title)
    b_title = TextBlob(submission.title.lower())
    if 'biden' in submission.title.lower():
        polarity = b_title.sentiment.polarity
        print('Biden = ', polarity)
        if polarity >= 0:
            submission.upvote()
            print('upvoting Biden positive submission')
        if polarity < 0: 
            submission.downvote()
            print('downvoting Biden negative submission')
    if 'trump' in submission.title.lower():
        polarity = b_title.sentiment.polarity
        print('republicans = ', polarity)
        if polarity < 0: 
            submission.upvote()
            print('upvoting Trump negative submission')
        if polarity >= 0:
            submission.downvote()
            print('downvoting Trump positive submission')

    for comment in submission.comments:
        blob = TextBlob(comment.body.lower())
        if 'biden' in comment.body.lower():
            polarity = blob.sentiment.polarity
            print('Biden = ', polarity)
            if polarity >= 0:
                comment.upvote()
                print('upvoting Biden positive comment')
            if polarity < 0: 
                comment.downvote()
                print('downvoting Biden negative comment')
        if 'trump' in comment.body.lower():
            polarity = blob.sentiment.polarity
            print('Trump = ', polarity)
            if polarity < 0: 
                comment.upvote()
                print('upvoting Trump negative comment')
            if polarity >= 0:
                comment.downvote()
                print('downvoting Trump positive comment')
    count += 1
    print("count =", count)



