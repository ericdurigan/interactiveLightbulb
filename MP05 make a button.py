# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:25:31 2021

@author: ericd
"""


import turtle

#Basic screen set up
screen = turtle.Screen()

screen.title("Creating a Button")
screen.bgcolor("red")
screen.tracer(0)

#Pen properties
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor("black")
pen.color("white")


#add mode
mode = "dark"

def drawButton(pen, message = "click me"):
    pen.penup()
    pen.begin_fill()
    pen.goto(ButtonX, ButtonY)
    pen.goto(ButtonX + ButtonLength, ButtonY)
    pen.goto(ButtonX + ButtonLength, ButtonY + ButtonWidth)
    pen.goto(ButtonX, ButtonY + ButtonWidth)
    pen.goto(ButtonX, ButtonY)
    pen.end_fill()
    pen.goto(ButtonX + 15, ButtonY + 15)
    pen.write(message, font = ('Arial', 15, 'normal'))
    

#Creating a rectangular button
ButtonX = -50
ButtonY = -50
ButtonLength = 100
ButtonWidth = 50

drawButton(pen)

def buttonClick(x,y):
    global mode
    if ButtonX <=x<=ButtonX +ButtonLength:
        if ButtonY <=y<=ButtonY +ButtonWidth:
            print("Clicked")
            if mode == 'dark':
                screen.bgcolor('green')
                mode = 'light'
            else:
                screen.bgcolor('red')
                mode = 'dark'
screen.onclick(buttonClick)


turtle.done()


