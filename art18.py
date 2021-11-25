"""

Welcome to the art series !

This version creates a position file to remember where the circles were

"""


import pygame 
import numpy as np
import random
from math import *

pygame.init()
pygame.mixer.init()

positions_file = open("positions.txt", "r+")



"""

These are the functions used in the program

colorChange fills the background with a color and can be used as a reset
playSound uses the stolen code to play a sin wave
drawCircle draws a circle with a border parameter

"""

def colorChange(background):
    
    window.fill(background)
    
    pygame.display.flip()

def drawCircle(color, position, radius, border_size, border_color, ring):
    
    if border_size != 0:
        
        pygame.draw.circle(window, border_color, position, radius + border_size)
        
    pygame.draw.circle(window, color, position, radius, ring)
    pygame.display.update()
    
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
    
    pygame.draw.rect(window, (0,0,0), (0,0,300,50))
    time = pygame.time.get_ticks() / 1000
    message = "Time in seconds: {}".format(time)
    window.blit(font.render(message, True, text_color), (10,10))

    message = "Mouse x: " + str(mousex) +  " Mouse y:" + str(mousey)
    window.blit(font.render(message, True, text_color), (10, 30))
        
    pygame.display.update()



"""

Here are the variables for initialization


"""



### Creates window ###

window_size = (1440,900)
window = pygame.display.set_mode((300,300), pygame.RESIZABLE)
pygame.display.set_caption("Funky Circle Time")

font = pygame.font.SysFont("Sans", 20)
text_color = (255,255,255)

colorChange((0,0,0))


### Random stuff ###

purple = (100, 0, 160)  
cyan = (0, 240, 255)  
black = (0,0,0)



### Variables for drawCircle function ###

radius = 100

color = cyan
position = (0,0)
radius = radius
border_size = 2
border_color = (0,0,0)
ring = radius



### Memory variables ###

theta = random.randint(0,360) * (2*pi/360)  
xmove = random.randint(0,window_size[0])
ymove = 0
last_color = 1300



### Variables to keep the loop going ###

running = True
play_Loop1 = False
play_Loop2 = False
play_Loop3 = False
keylist1 = "1234567890"
keylist2 = "qwertyuiop"



while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            
            running = False

            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:

            colorChange(black)
            
            
            

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and play_Loop1 == False:
            play_Loop1 = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and play_Loop1 == True:
            play_Loop1 = False            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and play_Loop2 == False:
            play_Loop2 = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and play_Loop2 == True:
            play_Loop2 = False            
            
            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            play_Loop3 = True
            
        
        
            

    if play_Loop1 == True:
            
            

        xmove += 10*cos(theta)
        ymove += 10*sin(theta)
        

        color = funkyMath(last_color)
        last_color += 5
        
        pos1 = (xmove, ymove)

    

        positions_file.write(str(pos1[0]) + "," + str(pos1[1]) + "\n")


        if pos1[0] > window_size[0] + radius or pos1[0] + radius < 0 or pos1[1] > window_size[1] + radius:
            
    
            xmove = random.randint(0,window_size[0])
            ymove = 0
            
            theta = random.randint(0,180) * (2*pi/360)  
            last_color = 1300



    if play_Loop2 == True:
        
        
        mousex, mousey = pygame.mouse.get_pos()
        showTime()

        

    if play_Loop3 == True:
        

      

        print(222)     
        
        x = positions_file.read()
        xs = x.split("\n")
        
        file_read = positions_file.read()
        file_split = file_read.split("\n")
        
        
        



        play_Loop3 = False
        






positions_file.close()
pygame.quit()
            















































































































































