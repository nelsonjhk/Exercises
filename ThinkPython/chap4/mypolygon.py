"""
    Successfully completed through 4.2
"""


import turtle
import math
wn = turtle.Screen()
#print(bob)

"""
for i in range(3):
    bob.fd(100)
    bob.rt(30)
    bob.bk(100)

square = turtle.Turtle()
for i in range(4):
    square.fd(100)
    square.rt(90)
"""
def arc(t, r, angle): #turtle, radius, angle
    # calculate circumference
    circ = 2*math.pi*r
    for i in range(angle):
        t.fd(circ/360)
        t.rt(1)

uncle = turtle.Turtle()
# arc(uncle,45,180)

def polyline(t, n, length, angle):
    """ Draws n line segments
    t: Turtle object
    n: number of sides/segments
    length: length of segments
    angle: degree turn
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def reversePolyline(t, n, length, angle):
    """ Draws n line segments
    t: Turtle object
    n: number of sides/segments
    length: length of segments
    angle: degree turn
    """
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def newArc(t, r, angle):
    circ = 2*math.pi*r
    arcLength = circ*angle/360
    n = int(arcLength / 3) + 1 # min segment of 1
    stepLength = arcLength / n
    stepAngle = float(angle) / n
    polyline(t, n, arcLength, stepAngle)
    t.lt(180)
    t.lt(-n*stepAngle)

def reverseArc(t, r, angle):
    circ = 2*math.pi*r
    arcLength = circ*angle/360
    n = int(arcLength / 3) + 1 # min segment of 1
    stepLength = arcLength / n
    stepAngle = float(angle) / n
    reversePolyline(t, n, arcLength, stepAngle)
# newArc(uncle, 20, 90)

# newArc(bob, 20, 90)

def flower(t, n, petalwidth, petalLength):
    """ Draws n petals in a flower shape.
    petal width adjusts size of the arc's circle
    petal length adjusts the angle of the arcs
    """
    petalAngle = int(360 / n)
    for i in range(n):
        newArc(t, petalwidth, petalLength)
        newArc(t, petalwidth, petalLength)
        t.rt(petalAngle)

def realflower(t, n, petalwidth, petalLength):
    """ Draws n petals in a flower shape.
    petal width adjusts size of the arc's circle
    petal length adjusts the angle of the arcs
    """
    petalAngle = int(360 / n)
    for i in range(n):
        newArc(t, petalwidth, petalLength)
        t.rt(180)
        reverseArc(t, petalwidth, 360-petalLength)
        t.rt(180 + petalAngle)
#flower(uncle, 4, 25, 30)
#flower(uncle, 8, 35, 40)
# realflower(uncle, 4, 25, 30)
def slice(t, length, sideAngle, baseLength):
    """ Draws a slice of turtle pie"""

    reversePolyline(t, 1, length, 180+sideAngle)
    reversePolyline(t, 1, baseLength, 180+sideAngle)
    polyline(t, 1, length, 180)


def pie(t, n, length):
    """ Draws turtle pies with n sections.

        t: Turtle object
        n: number of trianges
        length: length of an isoceles side of triangle.
        """

    innerAngle = 360.0 / n
    sideAngle = (180.0 - innerAngle) / 2.0
    sliceBase = 2 * length * math.sin(0.5 * innerAngle)
    for i in range(n):

        slice(t, length, sideAngle, sliceBase)
        t.lt(innerAngle)

# slice(uncle, 10, 60, 10)
# slice(uncle, 30, 75, 15)
bob = turtle.Turtle()
pie(bob, 6, 30)
uncle.hideturtle()
turtle.mainloop()
