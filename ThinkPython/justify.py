# This script rustifies all input strings to the 70th column.
import sys

string_input = str(sys.argv[1])

def right_justify(string):
    extra = 70 - len(string)
    print(' ' * extra, string)

right_justify(string_input)
