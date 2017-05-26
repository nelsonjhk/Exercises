""" This takes in two numbers and returns the greatest common denominator
"""
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("We need two arguments.")
    else:
        print(gcd(int(sys.argv[1]), int(sys.argv[2])))
