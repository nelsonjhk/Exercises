import turtle

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
turtle.mainloop()
