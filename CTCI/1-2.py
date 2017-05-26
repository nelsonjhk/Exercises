"""
Check permutation: take in 2 strings, write method to determine if one is permutation of another
"""

"""
Assume valid inputs
Base cases: 
    not equal length
    same string
One strategy: 
    sort strings then compare. Should be identical. 
    using efficient sorting, O(n log n)
"""

import sys

def compare(string1, string2):
    sorted1 = list(string1)
    sorted1.sort()
    sorted2 = list(string2)
    sorted2.sort()
    if sorted1 == sorted2:
        return True
    else: return False

if __name__ == "__main__":
    print(compare(sys.argv[1], sys.argv[2]))

"""
Grading: 
    Noted length-check optimization but did not implement.
    If efficiency is object, character counts is a solution. Make an array of available characters, then count number of times each appears in string1. Decrement while counting in string2. Remember ASCII character set is 128 large.  
