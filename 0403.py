"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random 
import numpy as np
import math 

def random_color():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return r,g,b

def draw_circle(radius, x0, y0, n=20):
    theta = 2*np.pi / n
    #angle_list = [0, theta*1, theta*2, theta*3, theta*4, theta*5]
    angle_list = []
    for i in range(n):
        angle_list.append(theta * i)

    x_list = []
    y_list = []
    for angle in angle_list:
        x = radius * math.cos(angle) + x0
        y = radius * math.sin(angle) + y0
        x_list.append(x)
        y_list.append(y)

    return x_list, y_list

font_list = pygame.font.get_fonts()
print(font_list)

훈민정음폰트 = pygame.font.Font('fonts/EBS훈민정음SB.ttf', 72)

# Define some colors
BLACK = (0, 0, 0)
WHITE = [255, 255, 100] # tuple 대신 list 를 사용해도 문제없다!
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
width = 2000
height = 1200
size = (width, height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("나의 파이게임 윈도우")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
FPS = 1 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
#    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    color = random_color()
    print(color, type(color))

    # pygame.draw.rect(screen, random_color(), [random.randrange(0, width),
    #                                 random.randrange(0, height),
    #                                 random.randrange(5, width//2),
    #                                 random.randrange(5, height//2)])


    xl, yl = draw_circle(200, 300, 400)
    for i in range(1, len(xl)):
        xp = xl[i-1]
        yp = yl[i-1]
        x = xl[i]
        y = yl[i]
        pygame.draw.line(screen, RED, [x,y], [xp, yp], 19)
    pygame.draw.line(screen, RED, [xl[0], yl[0]], [xl[-1], yl[-1]], 19)


    한글 = 훈민정음폰트.render("훈민정음SB 글꼴", True, (100, 200, 255))
    screen.blit(한글, (200, 200))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()