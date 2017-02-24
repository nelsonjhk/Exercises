import turtle
import math
wn = turtle.Screen()
bob = turtle.Turtle()
#print(bob)
for i in range(3):
    bob.fd(100)
    bob.rt(30)
    bob.bk(100)

square = turtle.Turtle()
for i in range(4):
    square.fd(100)
    square.rt(90)

def arc(t, r, angle): #turtle, radius, angle
    # calculate circumference
    circ = 2*math.pi*r
    for i in range(angle):
        t.fd(circ/360)
        t.rt(1)

uncle = turtle.Turtle()
arc(uncle,45,180)
turtle.mainloop()
