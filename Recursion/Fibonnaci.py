"""
Fibonnaci Sequence
Problem Statement: Implement a Fibonnaci Sequence in three different ways:

1. Recursively
2. Dynamically (Using Memoization to store results)
3. Iteratively
Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.

Else it returns fib(n-1)+fib(n+2).
"""

# Using Recursively
def fib_rec(n):
    if n == 0 or n == 1:
        return n

    return fib_rec(n-1) + fib_rec(n-2)


# Dynamically
n = 10
cache = [None] * (n+1)

def fib_dy(n):
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dy(n - 1) + fib_rec(n - 2)

    return cache[n]

# Iteratively

def fib_iter(n):

    # Setting Starting Points
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a

