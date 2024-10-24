#!/usr/bin/env python3
"""
The Redis module
"""
import sys
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4

import redis

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    system to count how many
    times methods of Cache class are called
    -param method:
    -return:
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrap
        -param self:
        -param args:
        -param kwargs:
        -return:
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    adding its input parameters to one list
    in redis and storing its output into another list
    -param method:
    -return:
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapp """
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper


class Cache:
    """
    the cache redis class
    """

    def __init__(self):
        """
        The constructor of redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        generatting random key (e.g. using uuid)-
         storring input data in Redis using
          random key and return the key
        -param data:
        -return:
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        """
        converting data back
        to the desired format
        -param key:
        -param fn:
        -return:
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """getting number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """getting string"""
        return self.decode("utf-8")
