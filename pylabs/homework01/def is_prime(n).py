def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    # PUT YOUR CODE HERE
    d = 2
    while n % d != 0:
        d += 1
    return d == n
    pass