import random
from turtle import right, window_height

from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.collision import *
from PPlay.gameimage import *

# Window
win_height = 600
win_width = 1000
win = Window(win_width, win_height)
title = win.set_title("Pong")
bgImg = GameImage("background.png")

# Ball
ball = Sprite("ball.png")
ball.x = (win_width/2)-(ball.width/2)
ball.y = (win_height/2)-(ball.height/2)
velx = 350
vely = 350

# LeftPlayer
leftPlayer = Sprite("player.png")
leftPlayer.x = 0
leftPlayer.y = (win_height/2) - (leftPlayer.height/2)

# RightPlayer
rightPlayer = Sprite("player.png", 1)
rightPlayer.x = win_width - rightPlayer.width
rightPlayer. y = (win_height/2) - (rightPlayer.height/2)

# PlayerVelocity
velp = 300

# Score
leftScore = 0
rightScore = 0

# Keyboard
keyboard = Window.get_keyboard()

while True:

    # Ball limits
    if(ball.y > win_height):
        vely *= -1
        if(vely > 0):
            vely *= -1
    if(ball.y < 0):
        vely *= -1
        if(vely < 0):
            vely *= -1
    
    # Player movement
    if(keyboard.key_pressed("UP") and rightPlayer.y >= 0):
        rightPlayer.y = rightPlayer.y - velp*win.delta_time()
    if(keyboard.key_pressed("DOWN") and rightPlayer.y + rightPlayer.height <= win_height):
        rightPlayer.y = rightPlayer.y + velp*win.delta_time()
    if(keyboard.key_pressed("W") and leftPlayer.y >= 0):
        leftPlayer.y = leftPlayer.y - velp*win.delta_time()
    if(keyboard.key_pressed("S") and leftPlayer.y + leftPlayer.height <= win_height):
        leftPlayer.y = leftPlayer.y + velp*win.delta_time()

    # Ball Collision
    if(ball.collided(rightPlayer)):
        velx *= -1
        if(velx > 0):
            velx *= -1
    if(ball.collided(leftPlayer)):
        velx *= -1
        if(velx < 0):
            velx *= -1

    # Scored
    if(ball.x < 0):
        rightScore += 1
        ball.x = (win_width/2)-(ball.width/2)
        ball.y = (win_height/2)-(ball.height/2)
        
        
    if(ball.x > win_width):
        leftScore += 1
        ball.x = (win_width/2)-(ball.width/2)
        ball.y = (win_height/2)-(ball.height/2)
        

    # Ball movement
    ball.x += velx * win.delta_time()
    ball.y += vely * win.delta_time()

    # Draw window elements
    bgImg.draw()
    ball.draw()
    leftPlayer.draw()
    rightPlayer.draw()
    win.draw_text('LEFT_SCORE: '+str(leftScore), 10, 10, size=12, color=('white'), font_name='Arial', bold=False, italic=False)
    win.draw_text('RIGHT_SCORE: '+str(rightScore), win_width-110, 10, size=12, color=('white'), font_name='Arial', bold=False, italic=False)
    win.update()