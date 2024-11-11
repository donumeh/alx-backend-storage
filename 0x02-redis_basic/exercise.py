#!/usr/bin/env python3

"""
Redis Client Creation
"""

import functools
import redis
from typing import Union, Optional, Callable, Any
from uuid import uuid4


def replay(method: Callable) -> None:
    """
    replay: retrieves all inputs and outputs
    of called by store method of Cache Class
    """
    key = method.__qualname__

    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)

    call_count = len(inputs)

    print(f"{key} was called {call_count} times:")

    for input_data, output_data in zip(inputs, outputs):
        print(f"{key}(*{input_data.decode()}) -> {output_data.decode()}")


def call_history(method: Callable) -> Callable:
    """
    call_history: records the input
    and output of a class method
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper: stores the input and output
        of a method into a list
        """
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count calls to methods of the Cache class
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper: increments the key
        """

        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a data value into a redis key

        data: the data to store
        """

        rand_key: str = str(uuid4())
        self._redis.set(rand_key, str(data))

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
