import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def setupWindow(wn):
  wn = turtle.Screen()
  wn.setworldcoordinates(-360,-1,360,1)
  wn.bgcolor("light blue")

def setupAxis(dart):  
  dart = turtle.Turtle()
  dart.hideturtle()
  dart.penup()
  dart.goto(0,-1.5)
  dart.pendown()
  dart.goto(0,1.5)
  dart.penup()
  dart.goto(-400,0)
  dart.pendown()
  dart.goto(400,0)
  
def drawSineCurve(dart):
  dart = turtle.Turtle()
  dart.hideturtle()
  dart.speed(2)
  dart.width(2)
  dart.penup()
  dart.goto(-360,0)
  for x in range (-360,361):
    dart.pendown()
    y = (math.sin(math.radians(x)))
    dart.goto(x,y)
  dart.clear()

def drawCosineCurve(dart):
  dart = turtle.Turtle()
  dart.hideturtle()
  dart.speed(2)
  dart.width(2)
  dart.penup()
  dart.goto(-360,1)
  for x in range (-360,361):
    dart.pendown()
    y = (math.cos(math.radians(x)))
    dart.goto(x,y)
  dart.clear()

def drawTangentCurve(dart):
  dart = turtle.Turtle()
  dart.hideturtle()
  dart.speed(2)
  dart.width(2)
  dart.penup()
  dart.goto(-360,0)
  for x in range (-360,361):
    dart.pendown()
    y = (math.tan(math.radians(x)))
    dart.goto(x,y)
  dart.clear()
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
