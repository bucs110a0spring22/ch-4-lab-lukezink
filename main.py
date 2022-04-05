import turtle
import math
import random
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def setupWindow(wn, bot_left_x=-360, bot_left_right=-1, top_right_x=360, top_right_y=1):
  """
	Sets up the window.
	Takes 4 integers, for the bottom left, bottom right, top left, and top right values
	"""
  wn.setworldcoordinates(bot_left_x, bot_left_right, top_right_x,top_right_y)
  wn.bgcolor("light blue")

def setupAxis(x_start=-400, y_start=-1.5, x_end=400, y_end=1.5):
  """
	Sets the axis in the window
	Takes 4 integers as args to draw lines along both axes.
	"""
  axis = turtle.Turtle()
  axis.speed(0)
  axis.hideturtle()
  axis.penup()
  axis.goto(0,y_start)
  axis.pendown()
  axis.goto(0,y_end)
  axis.penup()
  axis.goto(x_start,0)
  axis.pendown()
  axis.goto(x_end,0)
  
def drawSineCurve(dart):
  """
	Draws a sine curve.
	Takes a turtle to draw the curve.
	"""
  dart.hideturtle()
  dart.width(2)
  dart.penup()
  dart.goto(-360,0)
  for x in range (-360,361):
    dart.pendown()
    y = (math.sin(math.radians(x)))
    dart.goto(x,y)
  dart.clear()

def drawCosineCurve(dart):
  """
	Draws a cosine curve.
	Takes a turtle to draw the curve.
	"""
  dart.hideturtle()
  dart.width(2)
  dart.penup()
  dart.goto(-360,1)
  for x in range (-360,361):
    dart.pendown()
    y = (math.cos(math.radians(x)))
    dart.goto(x,y)
  dart.clear()

def drawTangentCurve(dart):
  """
	Draws a tangent curve.
	Takes a turtle to draw the curve.
	"""
  dart.hideturtle()
  dart.width(2)
  dart.penup()
  dart.goto(-360,0)
  for x in range (-360,361):
    dart.pendown()
    y = (math.tan(math.radians(x)))
    dart.goto(x,y)
  dart.clear()

def drawCircle(dart, rad=10):
  """
	Draws a circle.
	Takes a turtle, and a integer radius, and draws a circle of the given radius.
	"""
  dart.penup()
  dart.goto(0,-rad)
  dart.pendown()
  dart.circle(rad)

def getArea(rad=10):
  """
	Calculates the area of the circle.
	Takes an integer as the radius to calculate the area.
	Returns a float that is the area of the circle.
	"""
  PI = math.pi
  area = (rad^2)*PI
  return area

def guessArea(area, guess):
  """
	Takes the area and a guess and calculates the percent error.
  Takes the calculated area (float) and guess (int)
	Returns the area as a float value.
	"""
  
  if guess==area:
    print("Your guess has 0% error! Congratulations!")
  else:
    percent = abs(((area-guess)/guess)*100)
    print("Your guess has about a " + str(percent) + " percent error. Try again next time!")

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    setupWindow(wn)
    setupAxis()
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis()
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)

    #Midterm
    setupWindow(wn, -100,-100,100,100)
    radius = int(random.randrange(10,100,1))
    drawCircle(dart, radius)
    area = int(getArea(radius))
    guess = int(input("Please guess the area of the circle: "))
    guessArea(guess, area)
    wn.exitonclick()
main()
