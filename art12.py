"""

Welcome to the art series !

This version prints rainbow circles in random lines that don't go off screen

"""


import pygame 
import numpy as np
import random
from math import *

pygame.init()
pygame.mixer.init()

"""

Here are the variables for initialization


"""

### Creates window ###

window_size = (1440,900)
window = pygame.display.set_mode((300,300), pygame.RESIZABLE)
pygame.display.set_caption("Funky Circle Time")


### Random stuff ###

color1 = (100, 0, 160)  # Purple
color2 = (0, 240, 255)  # Cyan
black = (0,0,0)         # Black

play = False



### Variables for drawCircle function ###

color = color2
position = (0,0)
radius = 20
border_size = 2
border_color = (0,0,0)
ring = 20


### Variables for showTime funciton ###

font = pygame.font.SysFont("Sans", 20)
text_color = (255,255,255)

### Remebering positions for snake circles ###

position1 = (window_size[0]/2,window_size[1]/2)   # For position in the first keylist
starting_pos2 = (100,100)                         # For position in the second keylist

last_color = 0

"""

These are the functions used in the program

colorChange fills the background with a color and can be used as a reset
playSound uses the stolen code to play a sin wave
drawCircle draws a circle with a border parameter

"""

def colorChange(background):
    
    window.fill(background)
    
    pygame.display.flip()

colorChange(black)


def drawCircle(color, position, radius, border_size, border_color, ring):
    
    if border_size != 0:
        
        pygame.draw.circle(window, border_color, position, radius + border_size)
        
    pygame.draw.circle(window, color, position, radius, ring)
    
def funkyMath(track):
    
    while track <= 0:
        
        track += 1535
        
    while track > 1535:
        
        track -= 1535
        
    if track > 0 and track <= 255:
        red = 255 #255
        green = track #track
        blue = 0 #0       

    elif track > 255 and track <= 511:
        red = 511-track
        green = 255
        blue = 0        

    elif track > 511 and track <= 767:
        red = 0
        green = 255
        blue = track-512     

    elif track > 767 and track <= 1023:
        red = 0
        green = 1023-track
        blue = 255       

    elif track > 1023 and track <= 1279:
        red = track-1024
        green = 0
        blue = 255      

    elif track > 1279 and track < 1535:
        red = 255
        green = 0
        blue = 1535-track       
 
    elif track == 1535:
        red = 255
        green = 0
        blue = 0

    return red, green, blue

def showTime():
    
    pygame.draw.rect(window,color1, (0,0,300,30))
    time = pygame.time.get_ticks()
    message = "Time in ticks:" + str(time)
    window.blit(font.render(message, True, text_color), (10,10))


    
"""

The while running loop checks for keypress events

Press q-y for specific pentatonic notes

"""


keylist1 = "1234567890"
keylist2 = "qwertyuiop"

running = True

w = random.randint(0,360)    # for a random theta
u = w  * (2*pi/360)          # degrees to radians

theta = random.randint(0,360) * (2*pi/360)  

xmove = random.randint(0,window_size[0])
ymove = 0
last_color = 1300



while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
            
            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:

            for i in range(0,256):
                
                color = (i, i, i)
                colorChange(color)
                
            for i in range(0,256):
                
                color = (255-i, 255-i, 255-i)
                colorChange(color)
                
            colorChange(black)
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            
            xmove = random.randint(0,window_size[0])
            ymove = 0
            
            theta = random.randint(30,150) * (2*pi/360)  
            last_color = 1300


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and play == False:
            
            play = True
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and play == True:

            play = False                

    if play == True:
            
            
            
        startx = random.randint(0,window_size[0])
        starty = 0
        
        
        # xmove += 20*cos(u)
        # ymove += 20*sin(u)
        
        
        xmove += 10*cos(theta)
        ymove += 10*sin(theta)
        

        color = funkyMath(last_color)
        last_color += 5
        
        
        mousex, mousey = pygame.mouse.get_pos()
        
        print(mousex,mousey)
        
        # pygame.draw.rect(window,black, (0,20,300,20))
        # message = "Mouse x: " + str(mousex) +  " Mouse y:" + str(mousey)
        # window.blit(font.render(message, True, text_color), (20, 20))
        
        
        #pos = (mousex + xmove, mousey + ymove)

        #move = 20

        pos1 = (xmove, ymove)

    
        drawCircle(color,pos1,radius,border_size,border_color,ring)

        pygame.display.update()
        

        if pos1[0] > window_size[0] or pos1[0] < 0 or pos1[1] > window_size[1]:
            
    
            xmove = random.randint(0,window_size[0])
            ymove = 0
            
            theta = random.randint(0,180) * (2*pi/360)  
            last_color = 1300






