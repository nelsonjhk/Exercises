"""
Implements a sqrt estimator: mysqrt(x)

when run on its own, prints table comparing results to math.sqrt(x) 
"""

import math

def mysqrt(a):
    if a == 0:
        return 0
    return mysqrt_recurse(a, a/2)

def mysqrt_recurse(a, x):
    guess = (x + a/x)/2
    if abs(guess - x) < 0.0000000001:
        return guess
    else: return mysqrt_recurse(a, guess)

def printTable():
    print("a   mysqrt(a)     math.sqrt(a)   diff")
    print("_   _________     ____________   ____")
    for x in range(10):
        print(x, "   ", mysqrt(x), " ", math.sqrt(x), "   ", abs(mysqrt(x) - math.sqrt(x)))
if __name__ == "__main__":
    printTable()
