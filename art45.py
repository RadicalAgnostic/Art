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
Ver 37 - Changes to the keyboard
Ver 38 - startOnPerimeter Function
Ver 39 - startOnTop Function
Ver 40 - startOnMouse Function
Ver 41 - spray movement and squaresnake movement
Ver 42 - Bounce color pattern
Ver 43 - Fixed sizing bug
Ver 44 - Worm movement

Ver 45 - Long Worm movement

To do list: 
    
Mirror movement
Smart random generator
Length patterns
Flower patterns
Gui
frame rate
save image feature
remove circles
find when screen is covered
bouncing circles
expand circle data to all entries
add to funky math
circle count display
split auto draw into different functions
fix space bar

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
background_color = (0,0,0)


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

starting_pos1 = [0,0]                                  # Top left
starting_pos2 = [window_size[0], 0]                     # Top right
starting_pos3 = [0, window_size[1]]                     # Bottom left
starting_pos4 = [window_size[0], window_size[1]]        # Bottom right
starting_pos5 = [window_size[0]/2, 0]                   # Top middle
starting_pos6 = [window_size[0]/2, window_size[1]]      # Bottom middle
starting_pos7 = [window_size[0]/2, window_size[1]/2]    # Center




circle_data1 = [starting_pos1, 0, 0, 1]
circle_data2 = [starting_pos2, 0, 0, 1]
circle_data3 = [starting_pos3, 0, 0, 1]
circle_data4 = [starting_pos4, 0, 0, 1]
circle_data5 = [starting_pos5, 0, 0, 1]
circle_data6 = [starting_pos6, 0, 0, 1]
circle_data7 = [starting_pos7, 0, 0, 1]


color_direction = 1


random_total = 0
random_snake = 1
guided_down = 2
spray = 3
square_snake = 4
cross = 5
worm = 6
long_worm = 7 

rainbow = 100
slow_rainbow = 101

bounce = 10000


"""
--------------------------------------------
These are the functions used in the program
--------------------------------------------
"""

def funkyMath(track):
    """ Creates an rgb color scale """
    
    track = round(track)
    
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


def startOnPerimeter():
    
    perimeter = (window_size[0] * 2) + (window_size[1] * 2)
    
    x = random.randint(0,perimeter)
    
    
    
    if x <= window_size[0]:
        
        starting_pos = (x, 0)
    
    elif x <= window_size[0] + window_size[1]:
        
        x -= window_size[0]
        
        starting_pos = (window_size[0], x)
    
    elif x <= (window_size[0] * 2) + window_size[1]:
    
        x -= window_size[0] + window_size[1]
    
        starting_pos = (x, window_size[1])
        
    else:
        
        x -= (window_size[0] * 2) + window_size[1]
        
        starting_pos = (0, x)
        
        
        
    return starting_pos

def startOnTop():
    
    x = random.randint(0, window_size[0])
    
    starting_pos = (x, 0)
    
    return starting_pos

def startOnMouse():
    
    mouseX, mouseY = pygame.mouse.get_pos()
    
    starting_pos = (mouseX, mouseY)
    
    return starting_pos


def autoDraw(color, border_color, shade_range, starting_pos, movement = random_snake, length = 1000000000000000, circle_count = 0, last_color = 1, color_pattern = 0, color_direction = 1):
    """ Draws a bunch of circles """
    
    

    if circle_count == 0:
        
        last_color = color

    
    
    if circle_count <= length:
        
    
    
    
        circle_count += 1
        
        
        
        
        
    
    
        shade = random.randint(0, shade_range)
        
        
        
        
        
        if color_pattern == bounce:
            
            
            
            
            if last_color == color + shade_range:
        
                color_direction = -1
        
            elif last_color == color:
                
                color_direction = 1
        
        
            color = funkyMath(last_color)
            
            last_color = last_color + 1 * color_direction
        
        
        
        
        else:
            
    
            if color == white:
                
                color = (255 - shade, 255 - shade, 255 - shade)
        
            elif color == black:
                
                color = (shade, shade, shade)
                
            elif color == rainbow:
                
                
                color = funkyMath(last_color)
                
                last_color += 1
                
            elif color == slow_rainbow:
                
                
                color = funkyMath(last_color)
                
                last_color += 0.1
                
            else: 
                
                color = funkyMath(color + shade)
                
                
            
            
            
            
            
            
            
        if movement == random_snake:
            
            
            
            theta = random.randint(0,360)  * (2*pi/360)  
            xmove = radius * cos(theta)
            ymove = radius * sin(theta)
            pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
            
            
            drawCircle(color,pos,radius,border_size,border_color)
            
        if movement == random_total:        

            
            pos = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]
            
            drawCircle(color,pos,radius,border_size,border_color)
            
            
            
        if movement == guided_down:
             
            theta = random.randint(-85,265)  * (2*pi/360)  
            xmove = radius * cos(theta)
            ymove = radius * sin(theta)
            
            pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
            
            drawCircle(color,pos,radius,border_size,border_color)
            
            
            
            
        if movement == spray:
            
            theta = random.randint(0,360)  * (2*pi/360)  
            distance = random.randint(round(0.5*radius), round(3*radius))
            
            xmove = distance * cos(theta)
            ymove = distance * sin(theta)
            
            
            pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
            drawCircle(color,pos,radius,border_size,border_color)
            
            
            
            
        if movement == square_snake:
            

            y = random.randint(1,4)
            
            theta = (y * 90) * (2*pi/360)  
            xmove = radius * cos(theta)
            ymove = radius * sin(theta)
            

                

            pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
                
            
        
            drawCircle(color,pos,radius,border_size,border_color)
            
            
            
            
            
            
            
            
            
            
        if movement == cross:
            
            theta = random.randint(0,360)  * (2*pi/360)  
            distance = random.randint(round(3*radius), round(7*radius))
            
            xmove = distance * cos(theta)
            ymove = distance * sin(theta)
            
            
            pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
            
            
            
            ### center circle
            
            center_radius = 1.5 * radius
            
            drawCircle(color,pos,center_radius,border_size,border_color)
        
            ### side circles
            
            theta2 = random.randint(0,360)  * (2*pi/360)  
            distance2 = center_radius + radius
            
            xmove2= distance2 * cos(theta2)
            ymove2 = distance2 * sin(theta2)
            
            
            
            
            
            move = center_radius + radius
            
            left_pos = [pos[0] - xmove2, pos[1] + ymove2]
            right_pos = [pos[0] + xmove2, pos[1] + ymove2]
            top_pos = [pos[0]- xmove2, pos[1] - ymove2]
            bottom_pos = [pos[0] + xmove2, pos[1] - ymove2]
            
            
            drawCircle(color,left_pos,radius,border_size,border_color)
            drawCircle(color,right_pos,radius,border_size,border_color)
            drawCircle(color,top_pos,radius,border_size,border_color)
            drawCircle(color,bottom_pos,radius,border_size,border_color)
        
        
        
        
        
        if movement == worm:
            
            
            theta = random.randint(0,360)  * (2*pi/360)  
            distance = random.randint(round(3*radius), round(7*radius))
            
            xmove = distance * cos(theta)
            ymove = distance * sin(theta)
            
            
            first_radius = radius * 2
            
            first_pos = pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
            
            
            drawCircle(color,first_pos,first_radius,border_size,border_color)
            
            
            xmove2 = first_radius * cos(theta)
            ymove2 = first_radius * sin(theta)
            
            
            second_radius = radius * 1.5
            
            second_pos = [first_pos[0] + xmove2, first_pos[1] + ymove2]
            
            
            drawCircle(color,second_pos, second_radius,border_size,border_color)
            
            
            
            xmove3 = second_radius * cos(theta)
            ymove3 = second_radius * sin(theta)
            
            
            third_radius = radius 
            
            third_pos = [second_pos[0] + xmove3, second_pos[1] + ymove3]
            
            
            drawCircle(color,third_pos, third_radius,border_size,border_color)
            
            
        if movement == long_worm:
            
            theta = random.randint(0,360)  * (2*pi/360)  
            distance = random.randint(round(3*radius), round(7*radius))
            
            xmove = distance * cos(theta)
            ymove = distance * sin(theta)
            
            
            first_radius = radius * 2
            
            first_pos = pos = [starting_pos[0] + xmove, starting_pos[1] + ymove]
            
            
            
            
            xmove2 = first_radius * cos(theta)
            ymove2 = first_radius * sin(theta)
            
            
            second_radius = radius * 1.5
            
            second_pos = [first_pos[0] + xmove2, first_pos[1] + ymove2]
            
            
            
            
            
            xmove3 = second_radius * cos(theta)
            ymove3 = second_radius * sin(theta)
            
            
            third_radius = radius 
            
            third_pos = [second_pos[0] + xmove3, second_pos[1] + ymove3]
            
            
            
            
            xmove4 = third_radius * cos(theta)
            ymove4 = third_radius * sin(theta)
            
            
            fourth_radius = 0.75 * radius 
            
            fourth_pos = [third_pos[0] + xmove4, third_pos[1] + ymove4]
            
            
            
            xmove5 = fourth_radius * cos(theta)
            ymove5 = fourth_radius * sin(theta)
            
            
            fifth_radius = 0.5 * radius 
            
            fifth_pos = [fourth_pos[0] + xmove5, fourth_pos[1] + ymove5]
            
            
            
            
            drawCircle(color, [first_pos[0] + (first_pos[0] - fifth_pos[0]), first_pos[1] + (first_pos[1] - fifth_pos[1]) ], fifth_radius,border_size,border_color)
            drawCircle(color, [first_pos[0] + (first_pos[0] - fourth_pos[0]), first_pos[1] + (first_pos[1] - fourth_pos[1]) ], fourth_radius,border_size,border_color)
            drawCircle(color, [first_pos[0] + (first_pos[0] - third_pos[0]), first_pos[1] + (first_pos[1] - third_pos[1]) ], third_radius,border_size,border_color)
            drawCircle(color, [first_pos[0] + (first_pos[0] - second_pos[0]), first_pos[1] + (first_pos[1] - second_pos[1]) ], second_radius,border_size,border_color)
            
            
            drawCircle(color,first_pos,first_radius,border_size,border_color)
            drawCircle(color,second_pos, second_radius,border_size,border_color)
            drawCircle(color,third_pos, third_radius,border_size,border_color)
            drawCircle(color,fourth_pos, fourth_radius,border_size,border_color)
            drawCircle(color,fifth_pos, fifth_radius,border_size,border_color)
            
        
        
        
        
        if pos[0] > 0 and pos[0] < window_size[0]:      # checks x boundary
            starting_pos = [pos[0], starting_pos[1]]
            
        if pos[1] > 0 and pos[1] < window_size[1]:      # checks y boundary
            starting_pos = [starting_pos[0], pos[1]]
        
        
    starting_pos[0] = round(starting_pos[0])
    starting_pos[1] = round(starting_pos[1])
            
    circle_data = [starting_pos, circle_count, last_color, color_direction]
        
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

colorChange(background_color)

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
                
                
                
                
                colorChange(background_color)
                
                
            elif event.key == pygame.K_q:
                
                circle_data1[1] = 0
                circle_data2[1] = 0
                circle_data3[1] = 0
                circle_data4[1] = 0
                circle_data5[1] = 0
                circle_data6[1] = 0
                circle_data7[1] = 0
                
                circle_data1[2] = 0
                circle_data2[2] = 0
                circle_data3[2] = 0
                circle_data4[2] = 0
                circle_data5[2] = 0
                circle_data6[2] = 0
                circle_data7[2] = 0
                
                

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
                
                
                starting_pos1 = [0,0]                                   # Top left
                starting_pos2 = [window_size[0], 0]                   # Top right
                starting_pos3 = [0, window_size[1]]                     # Bottom left
                starting_pos4 = [window_size[0], window_size[1]]        # Bottom right
                starting_pos5 = [window_size[0]/2, 0]                   # Top middle
                starting_pos6 = [window_size[0]/2, window_size[1]]      # Bottom middle
                starting_pos7 = [window_size[0]/2, window_size[1]/2]    # Center
                
                
                circle_data1[0] = starting_pos1
                circle_data2[0] = starting_pos2
                circle_data3[0] = starting_pos3
                circle_data4[0] = starting_pos4
                circle_data5[0] = starting_pos5
                circle_data6[0] = starting_pos6
                circle_data7[0] = starting_pos7
                
                
                
            elif event.key == pygame.K_r:
                
                starting_pos1 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]                       
                starting_pos2 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]               
                starting_pos3 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]               
                starting_pos4 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]               
                starting_pos5 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]               
                starting_pos6 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]               
                starting_pos7 = [random.randint(0,window_size[0]), random.randint(0,window_size[1])]     
                
                circle_data1[0] = starting_pos1
                circle_data2[0] = starting_pos2
                circle_data3[0] = starting_pos3
                circle_data4[0] = starting_pos4
                circle_data5[0] = starting_pos5
                circle_data6[0] = starting_pos6
                circle_data7[0] = starting_pos7
                
                
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

                circle_data1[0] = starting_pos1
                circle_data2[0] = starting_pos2
                circle_data3[0] = starting_pos3
                circle_data4[0] = starting_pos4
                circle_data5[0] = starting_pos5
                circle_data6[0] = starting_pos6
                circle_data7[0] = starting_pos7
                



            elif event.key == pygame.K_p:
                
                
                circle_data1[0] = startOnPerimeter()
                circle_data2[0] = startOnPerimeter()
                circle_data3[0] = startOnPerimeter()
                circle_data4[0] = startOnPerimeter()
                circle_data5[0] = startOnPerimeter()
                circle_data6[0] = startOnPerimeter()
                circle_data7[0] = startOnPerimeter()
                
                
            elif event.key == pygame.K_t: 
                
                circle_data1[0] = startOnTop()
                circle_data2[0] = startOnTop()
                circle_data3[0] = startOnTop()
                circle_data4[0] = startOnTop()
                circle_data5[0] = startOnTop()
                circle_data6[0] = startOnTop()
                circle_data7[0] = startOnTop()
                
            elif event.key == pygame.K_m:
                
                circle_data1[0] = startOnMouse()
                circle_data2[0] = startOnMouse()
                circle_data3[0] = startOnMouse()
                circle_data4[0] = startOnMouse()
                circle_data5[0] = startOnMouse()
                circle_data6[0] = startOnMouse()
                circle_data7[0] = startOnMouse()

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
            
        

        
        
        circle_data1 = autoDraw(cyan, white, 400, circle_data1[0], \
                movement = long_worm, length = 10000000, circle_count = circle_data1[1], \
                last_color = circle_data1[2], \
                    color_pattern = bounce, color_direction = circle_data1[3] )
            
        # circle_data2 = autoDraw(black, white, 100, circle_data2[0], \
        #         movement = spray, length = 100000, circle_count = circle_data2[1],\
        #             last_color = circle_data2[2])
            
        # circle_data3 = autoDraw(white, black, 40, circle_data3[0], \
        #         movement = spray, length = 100000, circle_count = circle_data3[1],\
        #             last_color = circle_data3[2])
            
        # circle_data4 = autoDraw(1222, black, 200, circle_data4[0], \
        #         movement = spray, length = 10000000, circle_count = circle_data4[1], \
        #         last_color = circle_data4[2], \
        #             color_pattern = bounce, color_direction = circle_data4[3])

            

            


        pygame.display.update()
        

    if play_Loop2 == True:
        

        
        for i in range(0,1):
            
            circle_data7 = autoDraw(cyan, white, 400, circle_data7[0], \
                    movement = worm, length = 100000, circle_count = circle_data7[1],\
                        last_color = circle_data7[2], \
                            color_pattern = bounce, color_direction = circle_data7[3])
            
            
        pygame.display.update()
        
    





















