import tweepy
from config import Config

# Authenticate with Twitter API
client = tweepy.Client(
    bearer_token=Config.TWITTER_BEARER_TOKEN,
    consumer_key=Config.TWITTER_API_KEY,
    consumer_secret=Config.TWITTER_API_SECRET,
    access_token=Config.TWITTER_ACCESS_TOKEN,
    access_token_secret=Config.TWITTER_ACCESS_SECRET
)

# Fetch user details and tweets
def get_twitter_data():
    try:
        user = client.get_user(username="SarvarSing35025", user_fields=["public_metrics", "profile_image_url", "description"])
        tweets_response = client.get_users_tweets(user.data.id, tweet_fields=["public_metrics"], max_results=5)

        user_data = {
            "username": user.data.username,
            "name": user.data.name,
            "bio": user.data.description,
            "profile_image": user.data.profile_image_url,
            "followers": user.data.public_metrics["followers_count"],
            "following": user.data.public_metrics["following_count"],
            "tweets": []
        }

        if tweets_response.data:
            for tweet in tweets_response.data:
                user_data["tweets"].append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "likes": tweet.public_metrics["like_count"],
                    "retweets": tweet.public_metrics["retweet_count"]
                })

        return user_data
    except Exception as e:
        print(f"Twitter API Error: {e}")
        return {"username": "N/A", "followers": 0, "tweets": []}


# **Post a new Tweet**
def post_tweet(content):
    try:
        response = client.create_tweet(text=content)
        return response.data
    except Exception as e:
        print(f"Tweet Posting Error: {e}")
        return None