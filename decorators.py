import time
import logging
import math
import datetime

from iterators import my_range


def time_logger(func):
    def inner(*args, **kwargs):
        logging.basicConfig(filename='{}.{}.log'.format(func.__module__, func.__name__), level=logging.DEBUG)
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        logging.debug(
            "{}: func {} started at {} and took {}".format(datetime.datetime.now(), func.__name__, start, end - start))

    return inner


def my_square_root(size):
    for i in my_range(size):
        print(math.sqrt(i))


def timer(steps):
    for _ in my_range(steps):
        time.sleep(.1)


class BottleNeckDetector:
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        logging.basicConfig(filename='{}.{}.log'.format(
            self.original_func .__module__,
            self.original_func.__name__),
            level=logging.DEBUG
        )
        start = time.time()
        self.original_func(*args, **kwargs)
        end = time.time()
        logging.debug(
            "{}: func {} started at {} and took {}".format(datetime.datetime.now(), self.original_func.__name__, start, end - start))
        # return result
# my_square_root = time_logger(my_square_root)
# my_square_root(10000)
#
# timer = time_logger(timer)
# timer(40)
