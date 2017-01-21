# Functions to calculate the greatest common denominator of two (strictly)
# positive integers.
#
# Note that proper bad input handling should be implemented (with helper
# functions in case of the recursive implementations).


def sub_rec_GCD(n, m):

    if n == m:
        return n

    elif n > m:
        return sub_rec_GCD(m, n - m)

    else:
        return sub_rec_GCD(n, m - n)


def sub_iter_GCD(n, m):

    while n != m:

        if n > m:
            n = n - m

        elif m > n:
            m = m - n

    return n


def mod_rec_GCD(n, m):

    if m == 0:
        return n

    else:
        return mod_rec_GCD(m, n % m)


def mod_iter_GCD(n, m):

    while m != 0:
        mod = n % m
        n = m
        m = mod

    return n
