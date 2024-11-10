#!/usr/bin/env python3

"""
Redis Client Creation
"""

import redis
from typing import Union, Optional, Callable, Any
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

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a data value into a redis key

        data: the data to store
        """

        rand_key: str = str(uuid4())
        self._redis.set(rand_key, data)

        return rand_key

    def get(self, key: str, fn: Optional[Callable[[str], Any]] = None) -> Any:
        value = self._redis.get(key)

        if value is None:
            return None

        return fn(value) if fn else value

    def get_str(key: str) -> Optional[str]:
        """
        Returns a string of value passed
        """
        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(key: str) -> Optional[int]:
        """
        Returns an int of value passed
        """

        return self.get(key, fn=lambda d: int(d) if d else None)
