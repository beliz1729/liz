import math

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
    number = True
    i = 2
    while i <= math.sqrt(n): #квадратный корень, так как у простого числа 2 делителя - 1 и оно само
        if n % i == 0:
            number = False
            break
        else:
            i += 1
    return number