import os
from private import *
from api_helper import api_service
from helper import *
from datetime import date, datetime, timedelta

def main():
    # Logfile dir
    path = "D:/home/site/wwwroot/App_Data/jobs/triggered/test-write/test_bot"
    logfile = os.path.join(path, "retweets.log")

    # Set up with Twitter authentification.
    bod = api_service.ApiService(TWITTER_SCREEN_NAME, CUSTOMER_KEY, CUSTOMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, logfile)

    # Obtain and filter tweets.
    friends_ids = bod.get_friends()
    timelines = bod.get_friends_timelines(friends_ids)
    filtered_timelines = filter_timelines(timelines)

    # Calculate popularity and figure out the top tweets.
    followers_counts = bod.get_friends_follower_count(friends_ids)
    tweets = get_popular_tweets(filtered_timelines, followers_counts)

    # Post the top tweets.
    bod.retweet_many(tweets)

def filter_timelines(timelines, after=48, before=24):
    """ Filter out some statuses by some criteria """

    # Filter by time.
    before_time = datetime.today() - timedelta(hours=before)
    after_time = datetime.today() - timedelta(hours=after)
    new_timelines = filter_by_time(timelines, after_time, before_time)

    # Filter out retweets
    new_timelines = filter_by_creater(new_timelines)

    # Filter out reply-tweets
    new_timelines = filter_reply_tweets(new_timelines)

    return new_timelines


def get_popular_tweets(timelines, followers_counts, count=5):
    """ Get the top `count` of statuses """

    # Calculate popularity scores for each tweet
    popularity_scores = calculate_popularity(timelines, followers_counts)

    # Flattern the lists
    popularity_scores = [item for sublist in popularity_scores for item in sublist]
    tweets  = [item for sublist in timelines for item in sublist]

    # Sort the tweets by popularity scores
    popularity_indices = sorted(range(len(popularity_scores)),key=lambda x:popularity_scores[x], reverse=True)
    tweets_sorted = [tweets[i] for i in popularity_indices ]

    return tweets_sorted[0:count]

if __name__ == "__main__":
    main()
