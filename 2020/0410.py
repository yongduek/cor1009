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
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [800, 600]
screen_width, screen_height = SIZE
print('screen_geom: ', screen_width, screen_height)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
snow_list = []
snow_speed = [] # y --> [x, y]

snowflake_size = []

# Loop 50 times and add a snow flake in a random x,y position

for i in range(50):
    x = random.randrange(0, screen_width)
    y = random.randrange(0, screen_height)
    snow_list.append([x, y])
    snow_speed.append( [random.randrange(1, 10), random.randrange] )

print('snow_list: ]', snow_list)

def print_snow():
    for i in range(len(snow_list)):
        print(i, snow_list[i])

print_snow()

clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Process each snow flake in the list
    for i in range(len(snow_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 9)
 
        # Move the snow flake down one pixel

        snow_list[i][0] += snow_speed[i][0]
        snow_list[i][1] += snow_speed[i][1]
 
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > screen_height:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, screen_width)
            snow_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()