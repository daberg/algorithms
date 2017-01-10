# Function to compute factorial of a positive integer

def iter_fact(n):

    assert n > 0

    ris = 1

    while n > 0:
        ris = ris * n
        n = n - 1

    return ris

def rec_fact(n):

    if n == 0:
        return 1

    return n * rec_fact(n - 1)

def tail_rec_fact(n):

    return _tail_rec_fact(n, 1)

def _tail_rec_fact(n, res):

    if n == 0:
        return res

    return _tail_rec_fact(n - 1, res * n)

#print(iter_fact(10))
print(rec_fact(50))
#print(tail_rec_fact(10))

