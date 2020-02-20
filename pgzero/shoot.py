from random import randint 
import pgzrun 

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()
    print(apple.x, apple.y)

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    print("on_mouse_down: ", pos, type(pos))
    if apple.collidepoint(pos):
        print("Good Shot!")
        place_apple()
    else:
        print("You missed!")
        quit()
#

#place_apple()
pgzrun.go()