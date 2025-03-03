from flask import Flask, render_template, request, redirect, url_for
from utils.social_api import get_twitter_data, post_tweet

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tweet_content = request.form.get("tweet")
        if tweet_content:
            post_tweet(tweet_content)

    twitter_data = get_twitter_data()
    return render_template("index.html", twitter=twitter_data)

if __name__ == "__main__":
    app.run(debug=True)