# Functions to compute the nth Fibonacci number, i.e. the nth number in the
# Fibonacci sequence (with indexes starting at 0):
#
#     i  | 0   1   2   3   4   5   6   7   8   9  10  ...
# Fib(i) | 1   1   2   3   5   8  13  21  34  55  89  ...

def rec_fib(n):

    if n == 0 or n == 1: # Could be reduced to just n <= 1
        return 1

    return rec_fib(n - 1) + rec_fib(n - 2)

def tail_rec_fib(n):

    return _tail_rec_fib(1, 0, n)

def _tail_rec_fib(cur, prev, count):

    if count == 0:
        return cur

    return _tail_rec_fib(cur + prev, cur, count - 1)

def iter_fib(n):

    cur = 1
    prev = 0

    while n > 0:
        nxt = cur + prev
        prev = cur
        cur = nxt
        n = n - 1

    return cur

def memo_fib(n):

    results = [1, 1]

    for i in range(2, n + 1): 
        results.append(None)

    return _memo_fib(n, results)

def _memo_fib(n, results):

    if results[n] is None:
        results[n] = _memo_fib(n - 1, results) + _memo_fib(n - 2, results)

    return results[n]

for i in range(0,11):
    print(             str(i)
            + "\t" + str(rec_fib(i))
            + "\t" + str(tail_rec_fib(i))
            + "\t" + str(memo_fib(i))
            + "\t" + str(iter_fib(i))     )

