#!/usr/bin/python3
"""
This module counts the number of subscribers in a
particular sub-reddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Ge"
    ua += "cko/20100101 Firefox/100.0"
    headers = {"User-Agent": ua}
    try:
        sub_num = requests.get(url, headers=headers).json()
        sub_num = sub_num.get("data").get("children")
        sub_num = sub_num[0].get("data").get("subreddit_subscribers")
        return int(sub_num)
    except Exception as e:
        return 0
