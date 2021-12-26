"""

Welcome to the art series !


Ver 1  - prints rainbow circles with random motion
Ver 19 - black circle printing on the other side of screen
Ver 20 - circles run without holding down the key
Ver 21 - 4 rainbow circles
Ver 22 - tiny circles + bug fixes
Ver 23 - 2 rainbow circles, 1 black, 1 white
Ver 24 - Adds a random color shift to make the colors pop

Ver 25 - press return to restart circles in the corners

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

window_size = (1512, 982)
window = pygame.display.set_mode((300,300), pygame.RESIZABLE)
pygame.display.set_caption("Funky Circle Time")


### Colors ###

black = (0,0,0)
gray2 = (85,85,85)
gray1 = (170,170,170)
white = (255,255,255)

magenta = (255,0,128)
red = (255,0,0)
orange = (255,128,0)
yellow = (255,255,0)
mustard = (255,200,0)



pink = 1222
purple = 1093

### Variables for drawCircle function ###

color = black
position = (0,0)
radius = 20
border_size = 2
border_color = (0,0,0)



### Remebering positions for circles ###


starting_pos1 = (0,0)                                   # Top left
starting_pos2 = (window_size[0], 0)                     # Top right
starting_pos3 = (0, window_size[1])                     # Bottom left
starting_pos4 = (window_size[0], window_size[1])        # Bottom right

last_color = 0

"""
These are the functions used in the program
colorChange fills the background with a color and can be used as a reset
drawCircle draws a circle with a border parameter
funkyMath puts the rgb scale on one number line
"""

def colorChange(background):
    
    window.fill(background)
    
    pygame.display.flip()

def drawCircle(color, position, radius, border_size, border_color, ring = 100):
    
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

    elif track > 1279 and track <= 1535:
        red = 255
        green = 0
        blue = 1535-track       
 

    return red, green, blue


    
"""
The while running loop checks for keypress events

Space starts/stops the random circles
C resets window to background color (black)
Return starts the circles back in the corners

"""

colorChange(black)


play_Loop1 = False
running = True


while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
            
            
            
        if event.type == pygame.KEYDOWN:
            
            
            if event.key == pygame.K_c:
                
                colorChange(black)
        


            elif event.key == pygame.K_SPACE:
                
               if play_Loop1 == True:

                   play_Loop1 = False
                   
               elif play_Loop1 == False:
                   
                   play_Loop1 = True


            elif event.key == pygame.K_RETURN:
                
                
                starting_pos1 = (0,0)                                   # Top left
                starting_pos2 = (window_size[0], 0)                     # Top right
                starting_pos3 = (0, window_size[1])                     # Bottom left
                starting_pos4 = (window_size[0], window_size[1])        # Bottom right

                

    if play_Loop1 == True:
            
        ################ WHITE CIRCLE ################
            
        radius = 10
        border_size = 1
        border_color = black
        
        shade = random.randint(-40,0)

        color = (255 + shade, 255 + shade, 255 + shade)



        theta = random.randint(0,360)  * (2*pi/360)      # for a random theta

        xmove = radius * cos(theta)
        ymove = radius * sin(theta)
    
        pos1 = (starting_pos1[0] + xmove, starting_pos1[1] + ymove)




        if pos1[0] > 0 and pos1[0] < window_size[0]:
            starting_pos1 = (pos1[0], starting_pos1[1])
            
        if pos1[1] > 0 and pos1[1] < window_size[1]:
            starting_pos1 = (starting_pos1[0], pos1[1])
            
        

        drawCircle(color,pos1,radius,border_size,border_color)
        
        
        ################ PURPLE CIRCLE ################
        
        radius = 10
        border_size = 1
        border_color = white
        
        shade = random.randint(-100,100)

        color = funkyMath(purple + shade)



        theta = random.randint(0,360)  * (2*pi/360)      # for a random theta

        xmove = radius * cos(theta)
        ymove = radius * sin(theta)
    
        pos2 = (starting_pos2[0] + xmove, starting_pos2[1] + ymove)




        if pos2[0] > 0 and pos2[0] < window_size[0]:
            starting_pos2 = (pos2[0], starting_pos2[1])
            
        if pos2[1] > 0 and pos2[1] < window_size[1]:
            starting_pos2 = (starting_pos2[0], pos2[1])
            
        

        drawCircle(color,pos2,radius,border_size,border_color)
        
        
        
        
        ################ PINK CIRCLE ################
        
        
        radius = 10
        border_size = 1
        border_color = black
        
        shade = random.randint(-100,100)
        
        color = funkyMath(pink + shade)



        theta = random.randint(0,360)  * (2*pi/360)      # for a random theta

        xmove = radius * cos(theta)
        ymove = radius * sin(theta)
    
        pos3 = (starting_pos3[0] + xmove, starting_pos3[1] + ymove)




        if pos3[0] > 0 and pos3[0] < window_size[0]:
            starting_pos3 = (pos3[0], starting_pos3[1])
            
        if pos3[1] > 0 and pos3[1] < window_size[1]:
            starting_pos3 = (starting_pos3[0], pos3[1])
            
        

        drawCircle(color,pos3,radius,border_size,border_color)
        
        
        ################ BLACK CIRCLE ################
        
        
        radius = 10
        border_size = 1
        border_color = white
        
        


        shade = random.randint(0,100)

        color = (shade, shade, shade)


        theta = random.randint(0,360)  * (2*pi/360)      # for a random theta

        xmove = radius * cos(theta)
        ymove = radius * sin(theta)
    
        pos4 = (starting_pos4[0] + xmove, starting_pos4[1] + ymove)




        if pos4[0] > 0 and pos4[0] < window_size[0]:
            starting_pos4 = (pos4[0], starting_pos4[1])
            
        if pos4[1] > 0 and pos4[1] < window_size[1]:
            starting_pos4 = (starting_pos4[0], pos4[1])
            
        

        drawCircle(color,pos4,radius,border_size,border_color)
        
        
     


        pygame.display.update()
        

        
    




















