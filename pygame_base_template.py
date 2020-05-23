"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc

훈민정음 글꼴
 https://about.ebs.co.kr/kor/organization/font?tabVal=hunmin
"""

import numpy as np
import pygame
print (pygame.__version__)

# Define some colors
BLACK = (0, 0, 0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

font_list = pygame.font.get_fonts()
print(font_list)
font = pygame.font.SysFont('hy견고딕', 60)
훈민정음폰트 = pygame.font.Font('fonts/EBS훈민정음SB.ttf', 72)

# Set the width and height of the screen [width, height]
width, height = 700, 500
size = (width, height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
groot = pygame.image.load('groot.jpg')
print(type(groot))

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
FramesPerSecond = 60
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.get_pressed()
            print("User pressed a key.", key_pressed, len(key_pressed))
            if key_pressed[pygame.K_LEFT] == True:
                print("\tLeft Arrow Key Pressed.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print("User pressed a mouse button", mouse_pos)

    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.

#    screen.fill(WHITE)

    # --- Drawing code should go here
 
    # pygame.draw.rect(screen, 
    #             (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
    #             [random.randint(-10,width-1), random.randint(-10,height-1), random.randint(5,width), random.randint(5,height)]
    #     )

    # for _ in range(100):
    #     pygame.draw.rect(screen, 
    #                 (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
    #                 [random.randint(-10,width-1), random.randint(-10,height-1), 5, 5]
    #         )

    screen.blit(groot, (10, 20))

    text = font.render("한글 문자 시스템폰트", True, (255, 100, 200))
    screen.blit(text, (200, 100))

    한글 = 훈민정음폰트.render("훈민정음SB 글꼴", True, (100, 200, 255))
    screen.blit(한글, (200, 200))


    pygame.draw.arc(screen, BLUE, [300, 200, 200, 200], 0, np.pi)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(FramesPerSecond)
 
# Close the window and quit.
pygame.quit()