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
Ver 26 - names a bunch of colors for funkyMath function
Ver 27 - Adds 3 new starting points in the middle of window
Ver 28 - Experiment with mirror movement
Ver 29 - Mirror movement with 6 colors
Ver 30 - Press 1 to randomize position, Press 2 to switch positions
Ver 31 - The code looks pretty again!
Ver 32 - Fun new color scheme
Ver 33 - Movement patterns in the audtodraw funciton
Ver 34 - Movement patterns move indepenently
Ver 35 - Circle data tracks how many circles have been printed

Ver 36 - Circle data tracks the last color

"""

import pygame 
import numpy as np
import random
from math import *


pygame.init()
pygame.mixer.init()

"""
------------------------------------------
Here are the variables for initialization
------------------------------------------
"""

### Creates window ###

window_size = (1512, 982)
window = pygame.display.set_mode((300,300), pygame.RESIZABLE)
pygame.display.set_caption("Funky Circle Time")


### Colors ###



black = (0,0,0)
darkgray = (85,85,85)
lightgray = (170,170,170)
white = (255,255,255)

red             =    0  # used in funkyMath function
darkorange      =  100
lightorange     =  200
yellow          =  255
yellowgreen     =  300
lightgreen      =  400
green           =  500
bluegreen       =  600
cyan            =  700
lightblue       =  800
blue            =  900
darkblue        = 1000
purple          = 1093
pink            = 1222
hotpink         = 1300
magenta         = 1444


### Variables for drawCircle function ###

global radius
global border_size
radius = 10
border_size = 1

color = black
border_color = (0,0,0)
position = (0,0)


### Remebering positions for circles ###

starting_pos1 = (0,0)                                   # Top left
starting_pos2 = (window_size[0], 0)                     # Top right
starting_pos3 = (0, window_size[1])                     # Bottom left
starting_pos4 = (window_size[0], window_size[1])        # Bottom right
starting_pos5 = (window_size[0]/2, 0)                   # Top middle
starting_pos6 = (window_size[0]/2, window_size[1])      # Bottom middle
starting_pos7 = (window_size[0]/2, window_size[1]/2)    # Center


circle_data1 = (starting_pos1, 0, 0)
circle_data4 = (starting_pos4, 0, 0)


random_total = 0
random_snake = 1

rainbow = 100



"""
--------------------------------------------
These are the functions used in the program
--------------------------------------------
"""

def funkyMath(track):
    """ Creates an rgb color scale """
    
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



def colorChange(background):
    """ Sets the background color """
    
    window.fill(background)
    pygame.display.flip()


def drawCircle(color, position, radius, border_size, border_color, ring = 100):
    """ Draws a circle """
    
    if border_size != 0:
        
        pygame.draw.circle(window, border_color, position, radius + border_size)
        
    pygame.draw.circle(window, color, position, radius, ring)
    


circle_count1 = 0


def autoDraw(color, border_color, shade_range, starting_pos, movement = random_snake, length = 1000000000000000, circle_count = 0, last_color = 1):
    """ Draws a bunch of circles """
    
    



    
    
    if circle_count <= length:
        
    
        circle_count += 1
        
        
        
        
        
    
    
        shade = random.randint(0, shade_range)
        
    
        if color == white:
            
            color = (255 - shade, 255 - shade, 255 - shade)
    
        elif color == black:
            
            color = (shade, shade, shade)
            
        elif color == rainbow:
            
            
            color = funkyMath(last_color)
            
            last_color += 1
            
            
            
        else: 
            
            color = funkyMath(color + shade)
            
            
            
            
            
            
            
            
            
        if movement == random_snake:
            
            
            
            theta = random.randint(0,360)  * (2*pi/360)  
            xmove = radius * cos(theta)
            ymove = radius * sin(theta)
            pos = (starting_pos[0] + xmove, starting_pos[1] + ymove)
            
            

            
        if movement == random_total:        

            
            pos = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))
            
            drawCircle(color,pos,radius,border_size,border_color)
            
            
            
            
            
            
            
        
        drawCircle(color,pos,radius,border_size,border_color)
        
        
        if pos[0] > 0 and pos[0] < window_size[0]:      # checks x boundary
            starting_pos = (pos[0], starting_pos[1])
            
        if pos[1] > 0 and pos[1] < window_size[1]:      # checks y boundary
            starting_pos = (starting_pos[0], pos[1])
        
        
            
            
    circle_data = [starting_pos, circle_count, last_color]
        
    return circle_data




"""
--------------------------------------------------
The while running loop checks for keypress events
--------------------------------------------------

Space starts/stops the auto circles
Return starts the circles back in the corners

C resets window to background color (black)
1 randomizes the positions of the circles
2 swaps the positions of the cirlces

"""

colorChange((0,0,0))

### Variables to make the loop run ###
play_Loop1 = False
play_Loop2 = False
running = True


while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
            
            
        if event.type == pygame.KEYDOWN:
            
            
            if event.key == pygame.K_c:
                
                
                
                circle_data1 = [starting_pos1, 0, circle_data1[2]]
                circle_data4 = [starting_pos4, 0, circle_data4[2]]
                
                colorChange((0,0,0))
                
                
                
                
                

            elif event.key == pygame.K_1:
                
               if play_Loop1 == True:

                   play_Loop1 = False
                   
               elif play_Loop1 == False:
                   
                   play_Loop1 = True
        
                   
            elif event.key == pygame.K_2:
                
               if play_Loop2 == True:

                   play_Loop2 = False
                   
               elif play_Loop2 == False:
                   
                   play_Loop2 = True
                   
            elif event.key == pygame.K_SPACE:
                
               if play_Loop1 == True:

                   play_Loop1 = False
                   play_Loop2 = False
                   
               elif play_Loop1 == False:
                   
                   play_Loop1 = True
                   play_Loop2 = True
                   circle_count = 0


            elif event.key == pygame.K_RETURN:
                
                
                starting_pos1 = (0,0)                                   # Top left
                starting_pos2 = (window_size[0], 0)                     # Top right
                starting_pos3 = (0, window_size[1])                     # Bottom left
                starting_pos4 = (window_size[0], window_size[1])        # Bottom right
                starting_pos5 = (window_size[0]/2, 0)                   # Top middle
                starting_pos6 = (window_size[0]/2, window_size[1])      # Bottom middle
                starting_pos7 = (window_size[0]/2, window_size[1]/2)    # Center
                
                
            elif event.key == pygame.K_r:
                
                starting_pos1 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))                        
                starting_pos2 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))               
                starting_pos3 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))               
                starting_pos4 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))               
                starting_pos5 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))               
                starting_pos6 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))               
                starting_pos7 = (random.randint(0,window_size[0]), random.randint(0,window_size[1]))     
                
            elif event.key == pygame.K_s:
                
                x = starting_pos1
                starting_pos1 = starting_pos4
                starting_pos4 = x
                
                x = starting_pos2
                starting_pos2 = starting_pos3
                starting_pos3 = x
                
                x = starting_pos5
                starting_pos5 = starting_pos6
                starting_pos6 = x


            elif event.key == pygame.K_EQUALS:
                
                radius += 1
                
                if radius <= 10:
                    
                    border_size = 1
                    
                else:
                    
                    border_size = round(radius / 10)
                    
                    
            elif event.key == pygame.K_MINUS:
                
                
                if radius != 0:
                    radius -= 1
                
                if radius <= 10:
                
                    border_size = 1
                    
                else:
                    
                    border_size = round(radius / 10)
                    
            elif event.key == pygame.K_u:
                
                pygame.display.update()


    if play_Loop1 == True:
            
        

        
        
        circle_data1 = autoDraw(rainbow, black, 0, circle_data1[0], movement = random_snake, circle_count = circle_data1[1], last_color = circle_data1[2])
        # starting_pos2 = autoDraw(777, white, 100, starting_pos2)
        # starting_pos3 = autoDraw(darkblue, white, 100, starting_pos3)
        #starting_pos4 = autoDraw(black, white, 0, starting_pos4, movement = random_total)
        # starting_pos5 = autoDraw(white, black, 100, starting_pos5)
        # starting_pos6 = autoDraw(black, white, 40, starting_pos6)
           

        pygame.display.update()
        

    if play_Loop2 == True:
        
        circle_data4 = autoDraw(rainbow, white, 0, circle_data4[0], \
                movement = random_total, length = 10000, circle_count = circle_data4[1],\
                    last_color = circle_data4[2])
        pygame.display.update()
        
    




















