#HW_9 - Q1 & 3
#I have included the code for setting the background music and the code to play
#the next song when the first song ends in this code. I found the code in one of the 
#examples on the programarcadegames.com (example: graphics > background music)

import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 900x700 sized screen
screen = pygame.display.set_mode([900, 700])
 
# This sets the name of the window
pygame.display.set_caption('Finding Nemo')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
#click_sound = pygame.mixer.Sound("laser5.ogg")
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
background_image = pygame.image.load("fishtank.png").convert()
player_image = pygame.image.load("nemo.png").convert()
#sets black colour as transparent, making the imaging background also transparent
player_image.set_colorkey(BLACK)

#keyboard ASDW command
# Speed in pixels per frame - velocity 
x_speed = 0
y_speed = 0
 
# Current position - initial position
x_coord = 10
y_coord = 350
done = False

#importing sound file:
keyboard_sound = pygame.mixer.Sound ("fishbubbles.wav") 
pygame.mixer.music.load('Psychedelicacy.wav')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
#pygame.mixer.music.play()
while not done:

    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            #play the next song
            pygame.mixer.music.load('Bumper_Tag.ogg')
            pygame.mixer.music.play()
       #user pressed a key. resetting x,y cordinates inside the screen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if x_coord < 0:
                    x_coord = 0
                else:
                    x_speed = -5
            elif event.key == pygame.K_s:
                if y_coord >= 627:
                    y_coord = 627    
                else:
                    y_speed = 5
            elif event.key == pygame.K_d:
                if x_coord >= 799:
                    x_coord = 799    
                else:
                    x_speed = 5
            elif event.key == pygame.K_w:
                if y_coord <= 0:
                    y_coord = 0    
                else:
                    y_speed = -5          
           
        #User let up on a key
        elif event.type == pygame.KEYUP:
            #resetting vector back to zero 
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_s or event.key == pygame.K_w:
                y_speed = 0


    x_coord += x_speed
    y_coord += y_speed

##################################################################
# Position Check: 
# If you press K_a for a while, the coord will be updated without correction.
# Following codes fix such problems.
##################################################################
    if x_coord < 0: x_coord = 0
    if x_coord  > screen.get_rect().w - player_image.get_rect().w:
        x_coord = screen.get_rect().w - player_image.get_rect().w
    if y_coord < 0: y_coord = 0
    if y_coord > screen.get_rect().h - player_image.get_rect().h:
        y_coord = screen.get_rect().h - player_image.get_rect().h
##################################################################
    #playing sound when key pressed
    if event.type == pygame.KEYDOWN:
            keyboard_sound.play()      
      

    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
   # player_position = pygame.mouse.get_pos()
    #x = player_position[0]
    #y = player_position[1]
 
    # Copy image to screen:
    screen.blit(player_image, [x_coord, y_coord])
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
