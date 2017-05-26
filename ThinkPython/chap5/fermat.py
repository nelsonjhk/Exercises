import math
import sys

def checkFermat(a, b, c, n):
    if (a ** n + b ** n) == c ** n:
        if n <= 2: 
            print("That works as expected.")
        if n > 2: 
            print("You proved Fermat wrong!")
    else: 
        print("No, that doesn't work.")

if __name__ == "__main__":
    checkFermat(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
