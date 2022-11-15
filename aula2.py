#Mu Editor - Pygame Zero mode
import pgzrun
from pgzhelper import  *
from random import randint  #random int numbers

BG_COLOR = "#F5BB6B"

trophy = Actor('trophy')
frog = Actor('frog_idle')
pink = Actor('pink_idle')

trophy.scale = 1.5
frog.scale = 2
pink.scale = 2

def draw():
    screen.fill(BG_COLOR)

    trophy.draw()
    frog.draw()
    pink.draw()

def update():
    move_frog()
    move_pink()

    #Frog and Pink touch the Trophy
    frog_touchs_trophy = frog.collide_pixel(trophy)
    pink_touchs_trophy = pink.collide_pixel(trophy)

    if frog_touchs_trophy or pink_touchs_trophy:
        random_trophy()

''' debug collidepoint()
def on_mouse_down(pos):
    if rob.collidepoint(pos):
        print('Rob')
    else:
        print('Out')
'''

def random_trophy():
    trophy.x = randint(115, 700)
    trophy.y = randint(180, 500)

def move_frog():
    if keyboard.left:
        frog.x -= 2
    elif keyboard.right:
        frog.x += 2
    elif keyboard.up:
        frog.y -= 2
    elif keyboard.down:
        frog.y += 2
    '''
    elif keyboard.space:
        frog.x = 400
        frog.y = 300
    '''

def move_pink():
    if keyboard.a:
        pink.x -= 2
    elif keyboard.d:
        pink.x += 2
    elif keyboard.w:
        pink.y -= 2
    elif keyboard.s:
        pink.y += 2

pgzrun.go()  #run the code

#https://pyzero.cristianotito.repl.co/
#https://pygame-zero.readthedocs.io/
#images by Pixel Frog