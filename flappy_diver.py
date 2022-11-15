#Mu Editor - Pygame Zero mode
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

diver = Actor("diver_down")
diver.pos = (WIDTH / 2, HEIGHT / 2)

baiacu = Actor("baiacu")
baiacu.pos = randint(800, 1600), randint(10, 100)

tutu = Actor("tutu")
tutu.pos = randint(800, 1600), 450

up = False
game_over = False
life = 2
score = 0

def draw():
    if not game_over:
        screen.blit("background", (0, 0))
        screen.draw.text("Score: " + str(score), (700, 5), color="white")

        screen.draw.text("Life: " + str(life), (600, 5), color="white")

        diver.draw()
        baiacu.draw()
        tutu.draw()
    else:
        screen.fill("black")
        screen.draw.text("GAME OVER \nFinal score: " + str(score),
                         (WIDTH / 2, HEIGHT / 2),
                         color="white")

def update():
    global life, game_over

    diver_pos()
    baiacu_pos()
    tutu_pos()

    #collide
    diver_collide_baiacu = baiacu.colliderect(diver)
    diver_collide_tutu = tutu.colliderect(diver)

    if diver_collide_baiacu or diver_collide_tutu:
        life -= 1
        diver_pos_after_collide()

    if life == 0:
        game_over = True

def on_mouse_down():
    global up
    up = True
    diver.y -= 50
    diver.image = "diver_up"

def on_mouse_up():
    global up
    up = False
    diver.image = "diver_down"

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
        diver.y = HEIGHT / 2

def diver_pos_after_collide():
    diver.x = WIDTH / 4
    diver.y = HEIGHT / 2

pgzrun.go()