import itertools
import math
import random
import turtle
from turtle import Screen

bob = turtle.Turtle()
bob.speed(500)
screen = Screen()
OFFSETX = -300
OFFSETY = - 300
pperm =0.1# pixels per meter
turtlecoords= [0.0,0.0]

def move(x,y,write = True):
    if(write):
        bob.pd()
    else:
        bob.pu()
    global turtlecoords

    #norm is the distance to cover:
    norm = math.sqrt((x**2) + (y**2))
    if(norm == 0):
        return 0;

    #get the normalized vector for direction
    xnorm = x / norm
    ynorm = y / norm

    #get the angle
    radianangle = math.acos(xnorm)
    degangle = radianangle * 180 / math.pi
    angle = degangle
    if(ynorm < 0):
        angle = 360 - angle

    bob.lt(angle)
    bob.fd(norm * pperm)
    bob.rt(angle)

    turtlecoords[0] += x
    turtlecoords[1] += y
    return norm

def absmove(x,y,write = True):
    xrel = x - turtlecoords[0] + OFFSETX/pperm
    yrel = y - turtlecoords[1] + OFFSETY/pperm
    return move(xrel,yrel,write)

def cannon(x, dalpha, vzero):
    radalpha = dalpha * math.pi / 180
    return (-9.81 * x ** 2)/(2 * (vzero **2) * (math.cos(radalpha)**2) ) + x * math.tan(radalpha)

def grid():
    mindig = 500
    minpix = 5
    maxdig = 500
    maxpix = 10
    ranger = 50
    counter = 0
    index = 100
    absmove(0,0,False)
    for i in range(ranger):
        counter +=1*index
        move(1 * index,0)
        if(counter % maxdig == 0):
            move(0,maxpix / pperm)
            move(0,-maxpix / pperm)

        elif counter % mindig == 0:
            move(0,minpix / pperm)
            move(0,-minpix / pperm)
    absmove(0,0,False)
    for i in range(ranger // 3):
        counter +=1*index
        move(0,1* index)
        if(counter % maxdig == 0):
            move(maxpix / pperm,0)
            move(-maxpix / pperm,0)

        elif counter % mindig == 0:
            move(minpix / pperm,0)
            move(-minpix / pperm,0)
    absmove(0, 0, False)

def ballistic(angle):
    res = 50
    maxi = 0
    absmove(0,0,False)
    for x in range(2000):
        y = cannon(x * res, angle, 150)
        absmove(x * res, y)
        maxi = max(maxi,y)
        if y < 0:
            print("The mortar shell fell at a distance of  "+ str(x * res) + "m sir! Maximum height of the shell was "+str(int(maxi))+"m!")
            return x * res

def aim(min,max):
    val = random.randint(min,max)
    absmove(val,0,False)
    bob.color("green")
    absmove(val,25 / pperm)
    absmove(val,0,False)
    bob.color("blue")
    absmove(val - 25 ,0, False)
    move(0,25 / pperm)
    bob.color("blue")
    absmove(val + 25 ,0, False)
    move(0,25 / pperm)
    print("The target is at a distance of" + str(val)+ "!")
    return val

bob.speed(5000)
absmove(0, 0, False)
grid()
absmove(0, 0, False)
target = aim(790,2200)
absmove(0, 0, False)
bob.color("red")
#target is the distance to the target
#we must reach target within +- 25 meters of it
#we must find a correct angle
#//////////////////////////////////
#////////Write Code here///////////
#//////////////////////////////////

#//////////////////////////////////
#//////////////////////////////////
#//////////////////////////////////

turtle.mainloop()