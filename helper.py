
def filter_by_time(users_statuses, after, before):
    """ Filter the list of lists of Status objects by time """

    timelines_filtered = []
    for timeline in users_statuses:
        timeline_filtered = []
        for tweet in timeline:
            if tweet.created_at <= before and tweet.created_at >= after:
                timeline_filtered.append(tweet)
        timelines_filtered.append(timeline_filtered)

    return timelines_filtered


def filter_by_creater(users_statuses):
    """ Filter out retweets in the list of lists of Status objects """

    original_timelines = []
    for i, timeline in enumerate(users_statuses):
        original_statuses = []
        for tweet in timeline:
            if tweet.text[0:4] != "RT @":
                original_statuses.append(tweet)
        original_timelines.append(original_statuses)

    return original_timelines


def filter_reply_tweets(users_statuses):
    """ Filter out reply-tweets in the list of lists of Status objects """

    filtered_timelines = []
    for timeline in users_statuses:
        filtered_statuses = []
        for tweet in timeline:
            if tweet.in_reply_to_user_id == None:
                filtered_statuses.append(tweet)

        filtered_timelines.append(filtered_statuses)

    return filtered_timelines

def calculate_popularity(users_statuses, followers_counts):
    """ Calculate a popularity score for each Status in the list of lists of STatus """

    like_rates_users = []

    for i, timeline in enumerate(users_statuses):
        if followers_counts[i] > 0:
            like_rate = [ float(tweet.favorite_count + tweet.retweet_count)/followers_counts[i] for tweet in timeline ]
            like_rates_users.append( like_rate )

    return like_rates_users
