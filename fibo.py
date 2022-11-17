import functools
import timeit

def fiboGenerator():
    a = 0
    b = 1
    yield a 
    yield b
    while True:
        a, b = b, a + b
        yield b

def fiboCallGen(n):
    g = fiboGenerator()
    res = None
    for _ in range(n+1):
        res = next(g)
    return res


def fiboRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRec(n-1) + fiboRec(n-2)

@functools.lru_cache
def fiboRecCache(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecCache(n-1) + fiboRecCache(n-2)

if __name__ == '__main__':
    n = 40
    t1 = timeit.timeit(lambda: fiboCallGen(n), number=10)
    t2 = timeit.timeit(lambda: fiboRec(n), number=10)
    t3 = timeit.timeit(lambda: fiboRecCache(n), number=10)
    print(t1, t2, t3)