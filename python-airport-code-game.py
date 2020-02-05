# Turle Graphics Game - Space Turtle Camp
import turtle
import math
import random
import os
import time
import sched
from cities import cities
from threading import Timer

#Set Up Screen
turtle.setup(850,748)
wn = turtle.Screen()
wn.bgpic('world_map.gif')
wn.bgcolor('blue')
wn.tracer(3)

#Draw A Border
mypen = turtle.Turtle()
mypen.color('black')
mypen.penup()
mypen.setposition(-400,-199)
mypen.pendown()
mypen.pensize(3)
for s in range(2):
    mypen.forward(800)
    mypen.left(90)
    mypen.forward(398)
    mypen.left(90)
mypen.hideturtle()

#Draw title

#Create player turtle
player = turtle.Turtle()
player.color('black')
player.penup()
player.speed(0)

#Game Variables
score = 0
speed = 0
timeout = time.time() + 60

#Define Game Functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 0.75

def decrease_speed():
    global speed
    if speed > 1:
        speed -= 0.75

def isCollision(t1, t2):
    d  = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 30:
        return True
    else:
        return False

def draw(penname, x, y, text, font, size):
    penname.hideturtle()    
    penname.penup()
    penname.setposition(x, y)
    penname.write(text, align='left', font=(font, size))

#Set Keyboard Bindings
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')

#Initialize with first city
#Set first city as current city
current_city = random.choice(cities)

#display city code
citycodepen = turtle.Turtle()
citycodepen.color('black')
citynamepen = turtle.Turtle()
citynamepen.color('black')
citynamepen.hideturtle()
draw(citycodepen, -100, 255, "Find %s" % current_city['code'], 'Arial', 40)

#display score
scorepen = turtle.Turtle()
scorepen.color('black')
draw(scorepen, -120, -255, "Your Score: %s" % score, 'Arial', 40)

#display time
timepen = turtle.Turtle()
timepen.color('black')
draw(mypen, -180, -300, "Time Remaining:", 'Arial', 40)



#set city co-ordinates on the map
citypoint = turtle.Turtle()
# citypoint.color('black')
# citypoint.shape('circle')
# citypoint.shapesize(0.5)
citypoint.penup()
citypoint.hideturtle()
citypoint.setposition(current_city['x'], current_city['y'])


while time.time() < timeout:
    #Player
    player.forward(speed)

    timepen.undo()
    draw(timepen, 130, -300, str(int(timeout - time.time())), 'Arial', 40)

    #Player - Boundary Check
    if player.xcor() > 400:
        player.setposition(-400, player.ycor())
    if player.xcor() < -400:
        player.setposition(400, player.ycor())
    if player.ycor() > 200:
        player.setposition(player.xcor(), -200)
    if player.ycor() < -200:
        player.setposition(player.xcor(), 200)

    #Collision
    if isCollision(player, citypoint):
        #draw last city name
        citynamepen.undo()
        draw(citynamepen, -160, 230, "Good Job! That was %s!" % current_city['name'], 'Arial', 20)
        #add one point to score
        score += 1
        #change current city to another random city
        current_city = random.choice(cities)
        #reset coordinate
        citypoint.setposition(current_city['x'], current_city['y'])
        #change city name and score text
        citycodepen.undo()
        draw(citycodepen, -100, 255, "Find %s" % current_city['code'], 'Arial', 40)
        scorepen.undo()
        draw(scorepen, -120, -255, "Your Score: %s" % score, 'Arial', 40)

scorepen.setposition(0, 10)
scorepen.color("yellow")
scorestring = "Game Over: You Scored %s" % score
scorepen.write(scorestring, False, align="center", font=("Arial", 28, "normal"))
scorepen.setposition(0, -10)
scorestring = "CLICK TO EXIT"
scorepen.write(scorestring, False, align="center", font=("Arial", 14, "normal"))

wn.exitonclick()
