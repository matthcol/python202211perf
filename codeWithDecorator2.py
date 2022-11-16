import functools
from datetime import datetime

def twice(func):
    @functools.wraps(func)
    def twice_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        res = func(*args, **kwargs)
        return res
    return twice_wrapper

def timeit(func):
    @functools.wraps(func)
    def timeit_wrapper(*args, **kwargs):
        t1 = datetime.now()
        res = func(*args, **kwargs)
        t2 = datetime.now()
        delta = t2 - t1
        print("Execution time:", delta)
        return res
    return timeit_wrapper


@twice
@timeit
def fibo(n):
    @functools.lru_cache
    def _fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return _fibo(n-1) + _fibo(n-2)
    return _fibo(n)
