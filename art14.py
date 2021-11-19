"""

Welcome to the art series !

This version prints rainbow circles in random lines that have a slow color change

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

theta1 = random.randint(0,360) * (2*pi/360)  
theta2 = 90
xmove1 = random.randint(0,window_size[0])
ymove1 = 0
last_color1 = 1300
xmove2 = random.randint(0,window_size[0])
ymove2 = 0
last_color2 = 1300




left_corner = True  
right_corner = False
color1 = 0
color2 = 0

while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
            
            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:

            
            colorChange(black)
        

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and play == False:
            
            play = True
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and play == True:

            play = False                

    if play == True:
            
            
        
        pos1 = (xmove1, ymove1)
        pos2 = (xmove2, ymove2)

    
        if left_corner == True:
            
            drawCircle(color1,pos1,radius,border_size,border_color,ring)
            xmove1 += 10*cos(theta1)
            ymove1 += 10*sin(theta1)
            
            color1 = funkyMath(last_color1)
            last_color1 += 5
        


            if pos1[0] > window_size[0] or pos1[0] < 0 or pos1[1] > window_size[1]:
                
        
                xmove1 = 0
                ymove1 = 0
                
                theta1 = random.randint(0,90) * (2*pi/360)  
                last_color1 = 1100
                
                left_corner = False
                right_corner = True
                
        if right_corner == True:
            
            drawCircle(color2,pos2,radius,border_size,border_color,ring)
            xmove2 += 10*cos(theta2)
            ymove2 += 10*sin(theta2)
            
            color2 = funkyMath(last_color2)
            last_color2 += 5
        


            if pos2[0] > window_size[0] or pos2[0] < 0 or pos2[1] > window_size[1]:
                
        
                xmove2 = 1440
                ymove2 = 0
                
                theta2 = random.randint(90,180) * (2*pi/360)  
                last_color2 = 1100
                
                left_corner = True
                right_corner = False

        pygame.display.update()
        

























































































































































































































































































