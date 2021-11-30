# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:54:54 2021

@author: ericd
"""

"""The goal is to make a lightbulb that could light up multiple colors"""

import turtle
# =================== LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =======================
"""The objective here is to make an RGB lightbulb that is connected one corresponding button"""

"""MAKING THE LIGHTBULB"""
turtle.goto(0,100)
lightbulb = turtle.circle()
turtle.goto(0,0)
turtle.shape("square")
turtle.goto(0,-50)
turtle.shape("square")
turtle.goto(0,-100)
turtle.shape("square")


"""DIMENSIONS OF A BUTTON"""
class button(turtle.Turtle):
    
    def __init__(self):
        self.buttonColor1 = "red"
        self.buttonColor2 = "green"
        self.buttonColor3 = "blue"
        
        self.buttonShape = "circle"
        
    def buttonColors(self):
       
        """MAKING THE BUTTONS"""
        self.color(self.buttonColor1)
        redButton = turtle.circle(5)
        
        self.color(self.buttonColor2)
        greenButton = turtle.circle(5)
        
        self.color(self.buttonColor3 )        
        blueButton = turtle.circle(5)
        



"""CONNECTING THE BUTTONS TO THE LIGHTBULB"""
redButton.onclick.lightbulb("red")
blueButton.onclick.lightbulb("blue")
greenButton.onclick.lightbulb("green")
lightbulb("red")










turtle.circle(8)

turtle.mainloop()

turtle.done()



# ====================== FUNCTION DEFINITION =========================


    
    