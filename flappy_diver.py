import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

diver = Actor("diver")
diver.pos = (WIDTH/2, HEIGHT/2)

baiacu = Actor("baiacu")
baiacu.pos = randint(800, 1600), randint(10, 100)

tutu = Actor("tutu")
tutu.pos = randint(800, 1600), 450

up = False
score = 0

def draw():
    screen.blit("background", (0, 0))
    screen.draw.text(
        "Score: " + str(score),
        (700, 5),
        color="white"
    )

    diver.draw()
    baiacu.draw()
    tutu.draw()

def update():
    diver_pos()
    baiacu_pos()
    tutu_pos()

def on_mouse_down():
    global up
    up = True
    diver.y -= 50

def on_mouse_up():
    global up
    up = False

def baiacu_pos():
    if baiacu.x > 0:
        baiacu.x -= 1
    else:
        baiacu.pos = randint(800, 1600), randint(10, 100)

def tutu_pos():
    if tutu.x > 0:
        tutu.x -= 1
    else:
        tutu.pos = randint(800, 1600), 450

def diver_pos():
    #gravity
    if not up:
        diver.y += 1

    if diver.top < 0 or diver.bottom > 580:
        diver.y = HEIGHT/2

pgzrun.go()
#https://pygame-zero.readthedocs.io/en/stable/from-scratch.html

'''
TODO:
- score
- game over
- life
- levels
'''