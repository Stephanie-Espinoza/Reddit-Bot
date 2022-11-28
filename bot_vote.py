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
    if 'democrats' in submission.title.lower():
        polarity = b_title.sentiment.polarity
        print('democrats = ', polarity)
        if polarity >= 0:
            submission.upvote()
            print('upvoting democrat positive submission')
        if polarity < 0: 
            submission.downvote()
            print('downvoting democrat negative submission')
    if 'republicans' in submission.title.lower():
        polarity = b_title.sentiment.polarity
        print('republicans = ', polarity)
        if polarity < 0: 
            submission.upvote()
            print('upvoting republican negative submission')
        if polarity >= 0:
            submission.downvote()
            print('downvoting republican positive submission')

    for comment in submission.comments:
        blob = TextBlob(comment.body.lower())
        if 'democrats' in comment.body.lower():
            polarity = blob.sentiment.polarity
            print('democrats = ', polarity)
            if polarity >= 0:
                comment.upvote()
                print('upvoting democrat positive comment')
            if polarity < 0: 
                comment.downvote()
                print('downvoting democrat negative comment')
        if 'republicans' in comment.body.lower():
            polarity = blob.sentiment.polarity
            print('republicans = ', polarity)
            if polarity < 0: 
                comment.upvote()
                print('upvoting republican negative comment')
            if polarity >= 0:
                comment.downvote()
                print('downvoting republican positive comment')
    count += 1
    print("count =", count)



