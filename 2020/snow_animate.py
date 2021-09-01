"""
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/Gkhz3FuhGoI
"""

# Import a library of functions called 'pygame'
import pygame
import random
 
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [800, 600]

def draw_android(x, y):
    # pygame.draw.line(screen, GREEN, [x+])
    pygame.draw.circle(screen, RED, [x-45, y], 10)
    pygame.draw.circle(screen, RED, [x-15, y], 10)
    pygame.draw.rect(screen, GREEN, [x-45, y-20, 30, 20])
    pygame.draw.line(screen, RED, [x-30, y-20], [x-15, y-50], 7)
    pygame.draw.line(screen, RED, [x-30, y-20], [x-45, y-50], 7)

# Initialize the game engine
pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    snow_list.append([x, y])
 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLACK)

    pos = pygame.mouse.get_pos()
    print(pos)
    draw_android(pos[0], pos[1])

    # Process each snow flake in the list
    for i in range(len(snow_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 5)
 
        # Move the snow flake down one pixel
        snow_list[i][1] += random.randrange(0, 10)
        snow_list[i][0] += random.randrange(-5,5)

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > SIZE[1]:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, SIZE[0])
            snow_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()