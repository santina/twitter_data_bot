import tweepy as tp # Python wrapper for Twitter API
from time import gmtime, strftime # For logging time.

class ApiService(object):
    def __init__(self, name, customer_key, customer_secret, access_token, access_secret, logfile):
        auth = tp.OAuthHandler(customer_key, customer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tp.API(auth)
        self.name = name
        self.logfile = logfile

    def get_friends(self):
        """ Get a list of friend IDs """

        return self.api.friends_ids(self.name)

    def get_friends_follower_count(self, friends_ids):
        """ Get the count of followers of friends """

        followers_counts = []
        for friend_id in friends_ids:
            try:
                friend = self.api.get_user(friend_id)
                followers_counts.append(friend.followers_count)
            except tp.RateLimitError:
                time.sleep(15 * 60) # 15 minutes

        return followers_counts

    def get_friends_timelines(self, friends_ids, count=50):
        """ Get a number (count) of the most recent tweets posted by those friends of the given ids """

        timelines = []
        for friend_id in friends_ids:
            try:
                timeline = self.api.user_timeline(id=friend_id, count=count)
                timelines.append(timeline)
            except tp.RateLimitError:
                time.sleep(15 * 60)  # 15 minutes

        return timelines

    def retweet_many(self, tweets):
        for tweet in tweets:
            self.retweet(tweet.id_str)

    def retweet(self, tweet_id):
        # Send the tweet and log success or failure
        try:
            self.api.retweet(tweet_id)
        except tp.error.TweepError as e:
            print(e[0].message)
            self.log(tweet_id + " " + e[0].code + " " + e[0].message)
        else:
            self.log("Tweeted: " + tweet_id)

    def log(self, message):
        """ Append information to the log file """

        with open(self.logfile, 'a+') as f:
            time = strftime("%d %b %Y %H:%M:%S", gmtime())
            f.write(time + "; " + message + "\n")
