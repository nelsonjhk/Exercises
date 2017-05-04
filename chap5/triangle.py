def checkTriangle(a, b, c):
    if a + b > c or a + c > b or b + c > a: 
        print("This cannot be a triangle.")
    else:
        print("This may be a triangle.")

if __name__ == "__main__":
    print("Hello user. I can help check if your sides can make a triangle.")
    a = int(input("Please input a side length and hit 'Enter': \n"))
    b = int(input("Please input the next side length and hit 'Enter': \n"))
    c = int(input("Please input the last side length and hit 'Enter': \n"))
    checkTriangle(a, b, c)
