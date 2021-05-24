from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r], result:%r\n took: %2.4f sec' %
              (f.__name__, args, result, te - ts))
        return result

    return wrap
