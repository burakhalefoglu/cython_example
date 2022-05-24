from datetime import datetime
from functools import wraps


def performance_aspect(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        out = func(*args, **kwargs)
        end = datetime.now()
        dt = end - start
        print("{:.12f}".format(dt.total_seconds()))
        return out

    return wrapper
