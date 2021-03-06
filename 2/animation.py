# drawCircleArcExample.py     P. Conrad for CS5nm, 10/31/2008
#  How to draw an arc in Pygame that is part of a circle
from function_of_motion_correct import motion
import pygame
from pygame.locals import *
from sys import exit

import math

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))

# We need this if we want to be able to specify our
#  arc in degrees instead of radians
time_lapsed = 0;
def degreesToRadians(deg):
    return deg/180.0 * math.pi


# Draw an arc that is a portion of a circle.
# We pass in screen and color,
# followed by a tuple (x,y) that is the center of the circle, and the radius.
# Next comes the start and ending angle on the "unit circle" (0 to 360)
#  of the circle we want to draw, and finally the thickness in pixels

def drawCircleArc(screen,color,center,radius,startDeg,endDeg,thickness):
    (x,y) = center
    rect = (x-radius,y-radius,radius*2,radius*2)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)
   
    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)
    

white = (255,255,255);
gray = (50,50,50);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);
box = (80,198,196);
spring = (243,146,51);

m = 20
k = 3.
v = 0
p = 0

def print_config():
    global m
    global k
    if(m<=0):
        m = 1
    if (k<=0):
        k = 0.01    
    print('------------------------------')
    print('mass: {:.3f}'.format(m).rstrip("2")) 
    print('k   : {:.3f}'.format(k).rstrip("2")) 
    print('pos : {:.3f}'.format(p).rstrip("0")) 
    print('vel : {:.3f}'.format(v).rstrip("0")) 

while True:
    msElapsed = clock.tick(30)
    time_lapsed = time_lapsed+1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit();
        flag = False
	#mudando a posição
        if pygame.key.get_pressed()[pygame.K_w]:
            p = p + 1
            flag = True
        if pygame.key.get_pressed()[pygame.K_a]:
            p = p - 1
            flag = True
            
        #mudando a velocidade
        if pygame.key.get_pressed()[pygame.K_e]:
            v = v + 1
            flag = True
        if pygame.key.get_pressed()[pygame.K_s]:
            v = v - 1
            flag = True
            
        #mudando a constante de elasticidade
        if pygame.key.get_pressed()[pygame.K_r]:
            k = k + 2
            flag = True
        if pygame.key.get_pressed()[pygame.K_d]:
            k = k - 2
            flag = True
            
        #mudando a massa
        if pygame.key.get_pressed()[pygame.K_t]:
            m = m + 2
            flag = True
        if pygame.key.get_pressed()[pygame.K_f]:
            m = m - 2
            flag = True
            
        if flag:    
            print_config()
            time_lapsed = 0


    screen.fill(white);
    x = motion(m,k,p,v,time_lapsed)
     #line-spring
    pygame.draw.lines(screen, spring, False, [(200, 200),(200,270+x)], 5)
    
    pygame.draw.rect(screen, gray, (100,200,220,10), 0)
    
   
    
    
    #box
    pygame.draw.rect(screen, box, (180,270+x,40,40), 0)

    


    pygame.display.update()

    
