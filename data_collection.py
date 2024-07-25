import tweepy

def collect_tweets(api, query, count=100):
    """
    Collect tweets based on a search query.

    Parameters:
    api (tweepy.API): The Tweepy API object.
    query (str): The search query.
    count (int): The number of tweets to collect.

    Returns:
    list: A list of tweet texts.
    """
    tweets = api.search(q=query, count=count)  # Search for tweets
    return [tweet.text for tweet in tweets]  # Extract tweet text and return as list
