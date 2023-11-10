#!/usr/bin/python3
"""
print number of words keyword appears
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    this number queries reddit and print number of keyword appearances
    """
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Ge"
    ua += "cko/20100101 Firefox/100.0"
    headers = {"User-Agent": ua}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 302:
            # If the subreddit is invalid, print nothing
            return

        data = response.json()
        articles = data["data"]["children"]

        for article in articles:
            title = article["data"]["title"].lower()
            for word in word_list:
                # Check if the word is present in the title
                if f" {word.lower()} " in f" {title} ":
                    cd = count_dict.get(word.lower(), 0) + 1
                    count_dict[word.lower()] = cd

        after = data.get("data").get("after")
        if after is None:
            # Print the results in descending order by count
            sortedr = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sortedr:
                print(f"{word}: {count}")
            return

        # Recursive call to get the next page of results
        return count_words(subreddit, word_list, after, count_dict)
    except Exception as e:
        # Handle exceptions (e.g., network errors)
        return
