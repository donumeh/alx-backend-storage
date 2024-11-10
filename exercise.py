#!/usr/bin/env python3

"""
Redis Client Creation
"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    Creates a cache to store data
    """

    def __init__(self) -> None:
        """
        Store an instance of a Redis client
        and flush the instance
        """

        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:

        rand_key: str = str(uuid4())
        self._redis.set(rand_key, data)

        return rand_key



