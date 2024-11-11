#!/usr/bin/env python3

"""
Implementing an expiring web cache and tracker
"""

from datetime import timedelta
import functools
import requests
import redis
from typing import Callable


redis_client = redis.Redis()


def count_and_store(method: Callable) -> Callable:
    """
    count_and_store: counts the number of req made
    and store the values
    """

    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs):

        redis_client.incr(f"count:{url}")

        cached_content = redis_client.get(url)

        if cached_content:
            redis_client.expire(url, timedelta(seconds=10))
            return cached_content.decode('utf-8')

        result = method(url, *args, **kwargs)
        redis_client.setex(url, timedelta(seconds=10), result)

        return result

    return wrapper


@count_and_store
def get_page(url: str) -> str:
    """
    get_page: obtains the HTML content
    of a particular URL and returns it

    Args:
        url: the url to make a request to

    Return:
        the html content
    """
    res = requests.get(url)
    return res.text


if __name__ == "__main__":

    import time

    url = "http://google.com"

    for i in range(5):
        get_page(url)
        key = f"count:{url}"

        print(f"Saved value{i}: {redis_client.get(key).decode('utf-8')} \
                value: {redis_client.get(url).decode('utf-8')[:20]}")
        time.sleep(2)
