import turtle
import time

pol = turtle.Pen()
pol.shape('turtle')
pol.speed (100000)
turtle.bgcolor('blue')
def sd () :
    pol.penup()
    pol.right(50)
    pol.forward(20)
    pol.left(50)
    pol.pendown ()

a = 3
b = 120
c = 20
d = 30

pol.pendown ()

while True :
    if a == 8:
        exit()
    for i in range (a) :
      pol.left(b)
      pol.forward(c)
      time.sleep(0.5)
    sd ()

    a += 1 
    b = b - d 
    d -= 10 
    c = c + 20
