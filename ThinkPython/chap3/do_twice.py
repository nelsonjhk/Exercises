import sys

def do_twice(f, some_input):
    f(some_input)
    f(some_input)

def print_spam():
    print('spam')

def print_twice(a_string):
    print (a_string)
    print (a_string)

def print_four(a_string):
    print_twice(a_string)
    print_twice(a_string)

print_four('spam')
#do_twice(print_spam)


