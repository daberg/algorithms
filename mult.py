# Multiplication algorithm based on the fact that one factor can be expressed
# as a sum of powers of 2 (which is basically binary representation).


def mult(a, b):

    p = 0

    while a is not 0:

        # If the current power of two belongs to the a binary representation,
        # add the current b (initial b times the above power of two) to the
        # final result.
        if a % 2 is 1:
            p = p + b

        # Stepping to next power of two
        a = a // 2
        b = b * 2

    return p
