import turtle
from random import randint
a = int(input())
b = int(input())
c = int(input())

colors = ["red","blue","purple","green","white"]

screen = turtle.Screen()
Slave = turtle.Turtle()
screen.colormode(255)
screen.bgcolor("lightblue")
Slave.pensize(2)

def drawCircle(t,r,n,size):
    t.penup()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.pendown()
    for i in range(size):
        for i in range(n):
            for i in range(90):
                t.left(4)
                t.forward((2*3.14*r)/90)
            t.right(360/n)
        r += r/2
        t.right(360/size)
        Slave.color(randint(0,255),randint(0,255),randint(0,255))


drawCircle(Slave,a,b,c)
