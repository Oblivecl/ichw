import turtle
import math
def sin(x):
    y=math.sin(x)
    return y
def cos(x):
    y=math.cos(x)
    return y

###Ready###
wn=turtle.Screen()
wn.screensize(6000,6000)
turtle.bgcolor("black")
sun=turtle.Turtle()
mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()
plants=[mercury,venus,earth,mars,jupiter,saturn]

##Parameter setting
l=0.035   #orbital
ac=10000   #accuracy
si=0.5      #size
sp=300    #speed


###Color###
mercury.color("gray")
venus.color("yellow")
earth.color("blue")
mars.color("red")
jupiter.color("brown")
saturn.color("sea green")
sun.shape("circle")
sun.color("yellow")

###Shape###
sun.shapesize(69.5*0.1)
plants[0].shapesize(0.024397*si)
plants[1].shapesize(0.060518*si)
plants[2].shapesize(0.063710*si)
plants[3].shapesize(0.033895*si)
plants[4].shapesize(0.69911*si)
plants[5].shapesize(0.58232*si)
for i in range(6):
    plants[i].shape("circle")

###Orbital --ignore the angle between two orbitals major axis### 

##Starting position
for i in range(6):
    plants[i].penup()
    plants[i].speed(0)
plants[0].setpos(3.07/l,0)
plants[1].setpos(7.18/l,0)
plants[2].setpos(9.83/l,0)
plants[3].setpos(13.80/l,0)
plants[4].setpos(49.50/l,0)
plants[5].setpos(90.40/l,0)

##Period setting
for i in range(6):
    plants[i].pendown()

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0

for i in range(ac):
    plants[0].setpos((3.87*cos(a1)-0.80)/l,3.79/l*sin(a1))
    a1=a1+1/0.24/sp
    plants[1].setpos((7.23*cos(a2)-0.05)/l,7.23/l*sin(a2))
    a2=a2+1/0.615/sp
    plants[2].setpos((10.00*cos(a3)-0.167)/l,10.00/l*sin(a3))
    a3=a3+1/sp
    plants[3].setpos((15.23*cos(a4)-1.42)/l,15.16/l*sin(a4))
    a4=a4+1/1.88/sp
    plants[4].setpos((52.04*cos(a5)-2.54)/l,51.97/l*sin(a5))
    a5=a5+1/11.86/sp
    plants[5].setpos((95.83*cos(a6)-5.42)/l,95.76/l*sin(a6))
    a6=a6+1/29.46/sp
    

































