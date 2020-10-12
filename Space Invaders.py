# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:12:59 2020

@author: Golden Bird

SPACE INVADERS! 
TokyoEdTech tutorial
"""


import turtle
import math
import random
#from turtle import Turtle, Screen
#import os

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


#Draw border
border_pen = turtle.Turtle() #creates a border_pen Turtle object
border_pen.speed("fastest") #0 could also be used
border_pen.color("white") #sets the color
border_pen.pensize(3) #sets the size in pixels wide

border_pen.penup() #raises the pen so when the turtle moves it doesn't leave a trail
border_pen.setposition(-300,-300)
border_pen.pendown() #places the pen on the page so it leaves a trail when it moves

for side in range(4): #side could be any word, it is just a placeholder variable as you step through the for statement
    border_pen.forward(600)
    border_pen.left(90) #turns the turtle to the left by 90 degrees
    
border_pen.hideturtle()

#Set the score to 0
score = 0

#create the scoreboard
score_pen = turtle.Turtle()
score_pen.speed("fastest")
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.setposition(-290, 280)

scorestring = "Score: %s" %score #this is so the text we want to write can change
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
#the write command takes what will be written, if it moves, the alignment on the screen and the specifics of the font



#Create Player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.speed("fastest")

player.penup()
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


#Create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed("fastest")

bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = (20)

#bullet states
#   ready - ready to fire
#   fire - bullet is firing
bulletstate = "ready"




#Create an empty list of enimies
enemies = []
#Choose number of enemies
number_of_enemies = 5
#add enemies to list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.speed(0)

    enemy.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

    enemyspeed = 2




#Move the player
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Fire the bullet
def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        #position the bullet in front of the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        bulletstate = "fire"

#objects colliding 
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    

#Create Keybindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#Main Game Loop
while True:
    
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        #Move the enemy back and down
        if enemy.xcor() > 280:
            #moves all of the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            #changes the enemy's direction
            enemyspeed*= -1
            
    
            
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1
            
            
        #check if bullet hits enemy
        if isCollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy (FOR NOW!  IN THE FUTURE THIS CAN BE CHANGED)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            
            #update the score
            score += 10
            scorestring = "Score: %s" %score 
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            break
    
    #Move the bullet
    if bulletstate =="fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #reset bullet when it hits the top
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"
        

        

# PROBLEM IN WHILE LOOP.  GAME NEVER ENDS.  EXIT ON CLICK DOES NOT
# FUNCTION.  turtle.done() NEEDS TO BE RAN AFTER THE FORCE CLOSE
# OR THE PROGRAM WILL CRASH ON THE NEXT RUN.  FIX THIS BEFORE FINISH
    


wn.exitonclick()
turtle.done()
try:
    turtle.bye()   
except turtle.Terminator:
    pass