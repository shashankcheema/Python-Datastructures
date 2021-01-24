"""
Factorial Example:
4! = 4.3.2.1 = 4.3!
"""

def fact(n):

    if n == 0:
        return 1
    else:
        return n * fact(n-1)

