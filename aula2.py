#add Actor for giga
import pgzrun  #mu editor mode
from random import randint  #random int numbers

BG_COLOR = "#9469b5"

rob = Actor('robo')
dot = Actor('dot')
giga = Actor('giga')


def draw():
    screen.fill(BG_COLOR)

    rob.draw()
    dot.draw()
    giga.draw()


def update():
    move_dot()
    move_giga()

    #Dot touchs Rob
    dot_touchs_rob = dot.colliderect(rob)
    giga_touchs_rob = giga.colliderect(rob)

    if dot_touchs_rob or giga_touchs_rob:
        random_rob()


''' debug collidepoint()
def on_mouse_down(pos):
    if rob.collidepoint(pos):
        print('Rob')
    else:
        print('Out')
'''


def random_rob():
    rob.x = randint(115, 700)
    rob.y = randint(180, 500)


def move_dot():
    if keyboard.left:
        dot.x -= 2
    elif keyboard.right:
        dot.x += 2
    elif keyboard.up:
        dot.y -= 2
    elif keyboard.down:
        dot.y += 2
    '''
    elif keyboard.space:
        dot.x = 400
        dot.y = 300
    '''


def move_giga():
    if keyboard.A:
        giga.x -= 2
    elif keyboard.D:
        giga.x += 2
    elif keyboard.W:
        giga.y -= 2
    elif keyboard.S:
        giga.y += 2


pgzrun.go()  #run the code

#https://pyzero.cristianotito.repl.co/
#https://pygame-zero.readthedocs.io/
#images by Scratch
