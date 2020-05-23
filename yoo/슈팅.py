import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


#images

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("shooting game")


background_image = pygame.image.load(r"galaxy.png").convert()
player_image = pygame.image.load(r"ship.png").convert()
bullet_image = pygame.image.load(r"bullet.png").convert()
block_image = pygame.image.load(r"star.png").convert()

#background_image_rect = background.get_rect()

player_image.set_colorkey(BLACK)
bullet_image.set_colorkey(WHITE)
block_image.set_colorkey(WHITE)

# --- Classes

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self,color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.transform.scale(block_image,(50,40))
        self.rect = self.image.get_rect()

        #moving blocks horizontally
        self.rect.x = random.randrange(-100,-40)
        self.speed_x = random.randrange(1,6)
    
    def update(self) :
        self.rect.x += self.speed_x
        if self.rect.x > screen_width + 10 :
            self.rect.x = random.randrange(-100,-40)
            self.speed_x = random.randrange(1,10)
    


    
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = player_image
    
        self.rect = self.image.get_rect()
 
        
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.image = pos[0]
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = bullet_image
        self.rect = self.image.get_rect()
        
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# --- Create the window
 
# Initialize Pygame

pygame.init()

 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(50):
    # This represents a block
    block = Block(WHITE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.x = screen_width/2
player.rect.y = screen_height/2
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            pos=pygame.mouse.get_pos
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic
 
    # Call the update() method on all the sprites
    
    
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

 
    # --- Draw a frame

 
    # Draw all the spites
    background_position = [0, 0]
    screen.blit(background_image, background_position)

    #all_sprites_list.draw(screen)

    # screen.blit(player_image [player.rect.x, player.rect.y])
 
    # Go ahead and update the screen with what we've drawn.

   
    
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()