#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    print top 10 hot subreddits
    """
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Ge"
    ua += "cko/20100101 Firefox/100.0"
    headers = {"User-Agent": ua}
    try:
        sub_num = requests.get(url, headers=headers).json()
        sub_num = sub_num.get("data").get("children")
        for i in range(10):
            title = sub_num[i].get("data").get("title")
            print(title)
    except Exception as e:
        print(None)
