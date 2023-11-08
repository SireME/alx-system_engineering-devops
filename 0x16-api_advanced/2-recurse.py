#!/usr/bin/python3
"""
This modules returns all the hot articles in a subreddit
"""
import requests


def recurse(subreddit, after=None, hot_list=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Ge"
    ua += "cko/20100101 Firefox/100.0"
    headers = {
            "User-Agent": ua
            }

    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data["data"]["children"]

        if not articles:
            return hot_list

        for article in articles:
            hot_list.append(article["data"]["title"])

        after = data.get("data").get("after")
        if after is None:
            return hot_list
        # Recursive call to get the next page of results
        return recurse(subreddit, after, hot_list)
    except Exception as e:
        return None
