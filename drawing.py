# drawing.py
# ----------
# By Louis Cooper
# This is a drawing of a turtle race!

from turtle import *
import random

raceDistance = 705 #global speed variable for turtles
drawingTurtleSpeed = 10
ht()               #documentation states that ht should speed up drawing by hiding turtle, no noticeable change here, just makes clouds look laggy
screenSize = screensize() #400px x 300px screen size, unable to change size it seems?
bgcolor("black")
penup()
setpos(-400, -400) #sets position of turtle

def drawGround(): #draws the ground utilizing a for loop and turtle methods
    pendown()
    speed(drawingTurtleSpeed)     #changes speed of ALL turtles, not cloud turtle for some reason.
    for i in range(2):
        fillcolor("#AFE1AF")
        begin_fill()
        forward(800)
        left(90)
        forward(200)
        left(90)
        end_fill()
    penup()
    left(90)
    forward(200)

def drawSky(): #draws the sky using a for loop and turtle methods
    pendown()
    for i in range(2):
        fillcolor('blue')
        begin_fill()
        forward(800)
        right(90)
        forward(800)
        right(90)
        end_fill()
    penup()

def drawSingleCloud():
    cloudCircleSize = 25;
    penup()            #pen remains up but fillcolor still is functional
    for i in range(5):
        fillcolor("white")
        pencolor(0,0,0)
        begin_fill()
        circle(cloudCircleSize)
        right(25)
        left(90)
        forward(45)
        circle(cloudCircleSize)
        end_fill()

def drawClouds():
    speed(drawingTurtleSpeed)
    setpos(300, 300)
    drawSingleCloud()
    setpos(200, 175)
    drawSingleCloud()
    setpos(2, 75)
    drawSingleCloud()
    setpos(-200, 75)
    drawSingleCloud()
    setpos(-300, 275)
    drawSingleCloud()

def turtleLineup():  
    turtle1 = Turtle()
    turtle1.penup()
    turtle1.hideturtle()
    turtle1.setpos(-370, -330)
    turtle1.color("black")
    turtle1.shape("turtle")
    turtle1.showturtle()
    turtle1.speed(1)

    turtle2 = Turtle()
    turtle2.penup()
    turtle2.hideturtle()
    turtle2.setpos(-370, -300)
    turtle2.color("red")
    turtle2.shape("turtle")
    turtle2.showturtle()
    turtle2.speed(2)

    turtle3 = Turtle()
    turtle3.penup()
    turtle3.hideturtle()
    turtle3.setpos(-370, -270)
    turtle3.color("purple")
    turtle3.shape("turtle")
    turtle3.showturtle()
    turtle3.speed(3)

    turtle4 = Turtle()
    turtle4.penup()
    turtle4.hideturtle()
    turtle4.setpos(-370, -240)
    turtle4.color("yellow")
    turtle4.shape("turtle")
    turtle4.showturtle()
    turtle4.speed(4)
    return turtle1, turtle2, turtle3, turtle4

def startRace():
    t1.forward(raceDistance)
    t2.forward(raceDistance)
    t3.forward(raceDistance)
    t4.forward(raceDistance)
    
drawGround()
drawSky()  
drawClouds()
t1, t2, t3, t4 = turtleLineup() #Utilizes the returned turtle objects for methods like distances see: startRace()
startRace()
input()
