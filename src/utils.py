import time
from contextlib import contextmanager
import logging

logger = logging.getLogger()

@contextmanager
def timer(message):
    """to calculate timing ref: https://www.learndatasci.com/solutions/python-timer/"""
    t_0 = time.perf_counter()
    try:
        yield
    finally:
        t_1 = time.perf_counter()
        elapsed = t_1 - t_0
        logger.info('%s %0.4f',message ,elapsed)

class SingletonClass(type):
    """add this class as metaclass for make it singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
