#CrossRoads Turtle Game
#Creator: Oliver Cheng

import turtle
from turtle import *
import math

velocity = 3


#Lives, every time they hit a obstacle, they lose a life

lives = 3



#Draws title screen without showing steps(appears instantly)
ex = turtle.Screen()
ex.bgcolor('red')
ex.tracer(4)

#Function to draw the level base
def drawrectangle():
    title.fillcolor('green')
    title.begin_fill()
    for i in range(2):
        title.forward(500)
        title.left(90)
        title.forward(100)
        title.left(90)
    title.end_fill()


#Cover page
title = turtle.Turtle()
title.penup()
title.setposition(-300,200)
title.pendown()

#Border of game
drawrectangle()
for i in range(4):
    for i in range(2):
        title.forward(500)
        title.right(90)
        title.forward(50)
        title.right(90)
    title.right(90)
    title.forward(50)
    title.left(90)

title.fillcolor('green')
title.begin_fill()

for i in range(2):
    title.forward(500)
    title.right(90)
    title.forward(100)
    title.right(90)
title.end_fill()





#Player sprite
sprite = turtle.Turtle()
sprite.penup()
sprite.left(90)
sprite.setposition(-75,-25)
sprite.speed(0)

#Obstacles put in list to make it simpler
obstacle = ['one','two','three','four',]
obstacle[0] = turtle.Turtle()
obstacle[0].penup()
obstacle[0].setposition(-75,25)
obstacle[0].shape('triangle')
obstacle[0].speed(3)

obstacle[1] = turtle.Turtle()
obstacle[1].penup()
obstacle[1].left(180)
obstacle[1].setposition(-25,75)
obstacle[1].shape('circle')
obstacle[1].speed(3)

obstacle[2] = turtle.Turtle()
obstacle[2].penup()
obstacle[2].setposition(-250,125)
obstacle[2].shape('circle')
obstacle[2].speed(3)

obstacle[3] = turtle.Turtle()
obstacle[3].left(180)
obstacle[3].penup()
obstacle[3].setposition(100,175)
obstacle[3].shape('circle')
obstacle[3].speed(3)


ex.update()



#Removes the delay from the ex.tracer instruction

def goforward():
       
    ex.update()
    sprite.forward(50)
    #Keeps player on the gamescreen
    if sprite.xcor() >= 200 or sprite.xcor() <= -300:
        sprite.back(50)
    if sprite.ycor() >= 300 or sprite.ycor() <= -100:
        sprite.back(50)
 

def goback():
    ex.update()
    sprite.back(50)
    if sprite.xcor() >= 200 or sprite.xcor() <= -300:
        sprite.forward(50)
    if sprite.ycor() >= 300 or sprite.ycor() <= -100:
        sprite.forward(50)
    

def turnright():
    #ex.update()
    sprite.right(90)
    sprite.forward(50)
    sprite.left(90)
    if sprite.xcor() >= 200 or sprite.xcor() <= -300:
        sprite.left(90)
        sprite.forward(50)
        sprite.right(90)
    if sprite.ycor() >= 300 or sprite.ycor() <= -100:
        sprite.left(90)
        sprite.forward(50)
        sprite.right(90)

#go left
def turnleft():
    ex.update()
    sprite.left(90)
    sprite.forward(50)
    sprite.right(90)
    if sprite.xcor() >= 200 or sprite.xcor() <= -300:
        sprite.right(90)
        sprite.forward(50)
        sprite.left(90)
    if sprite.ycor() >= 300 or sprite.ycor() <= -100:
        sprite.right(90)
        sprite.forward(50)
        sprite.left(90)


#Collision formula, this will know if two turtles are touching
def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
    

    



# keybinds
onkey(goforward, 'Up')
onkey(goback, 'Down')
onkey(turnright, 'Right')
onkey(turnleft, 'Left')
#tells the turtle to act when a key is pressed a hard
listen()


while lives > 0:
    ex.update()
    obstacle[0].forward(5)
    obstacle[1].forward(5)
    obstacle[2].forward(5)
    obstacle[3].forward(5)
    if obstacle[0].xcor() >= 200 or obstacle[0].xcor() <= -300:
        #ex.update()
        obstacle[0].right(180)

    if obstacle[1].xcor() >= 200 or obstacle[1].xcor() <= -300:
        #ex.update()
        obstacle[1].right(180)

    if obstacle[2].xcor() >= 200 or obstacle[2].xcor() <= -300:
        #.update()
        obstacle[2].right(180)

    if obstacle[3].xcor() >= 200 or obstacle[3].xcor() <= -300:
        ex.update()
        obstacle[3].right(180)

    if isCollision(obstacle[0],sprite) or isCollision(obstacle[1],sprite) or isCollision(obstacle[2],sprite) or isCollision(obstacle[3],sprite) :
        sprite.setposition(-75,-25)
        lives = lives - 1
        print('you died!')

print('you lose!')
#ends the game
if lives == 0:
    raise SystemExit
        




















mainloop()




        
    
        
    














    



