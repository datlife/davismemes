from bots.reddit import RedditMemeBot


if __name__ == "__main__":
    reddit_bot = RedditMemeBot('UCDavis', 'ClShg45mn9UHxw', 'h9TDXwNUT3X5xUUVI3WgIficOKA')
    for p in reddit_bot.get_latest_memes(limit=10):
        print("{},".format(p))

    for p in reddit_bot.get_hottest_memes(limit=10):
        print("{},".format(p))