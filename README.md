## Learning experience

For now though, I just want to learn how to make a twitter bot.

There are many ways to do this. I'll try different ways until I'm very familiar with making Twitter bots.

## First step (this repo)

Create a twitter bot using Python.

## End goal

The aim is to create a twitter bot that will find top data scientists to follow, and retweet the best tweets among their tweets.

The bot should be generalizable to other fields.

In other word, a bot that can follow most informative people of a specific field and retweet their tweets. This can help people get information easier without having to figure out who to follow.

## Version 0.0.1

### Name of the bot

Let's call it Bod for now. Bod stands for "Bot of data science".

### Working condition

Bod looks for its friends tweets that have existed for at least 24 hours but no more than 48 hours. Bod ignores any retweets and reply-tweets, and gives a popularity score to each tweet. Bod will then retweet the top 5 tweets. It does this every day.

Popularity is measured by the ratio of the combined counts of likes and retweets to the number of followers.

### Flaws
- Dealing with tweets that are replies to other tweets
  - Should the popularity scores get combined or what?
  - There are quality reply-tweets, but dealing with them requires aggregating related tweets somehow and potentially violating the time constraint that ensures the freshness of the tweets.
- Cannot auto-follow people. This part is done manually at the moment
  - At some point, Bod needs to grow up and know how to find good people to follow by itself.


### CRON job

This is what make Bod a robot. It's running on Azure.
