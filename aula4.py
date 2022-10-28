import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

alien = Actor("alien")
alien.pos = (WIDTH/2, HEIGHT-50)

planeta = Actor("planeta")
planeta.pos = (randint(0, 800), -10)

score = 0
life = 2
game_over = False

def draw():
    screen.blit("space", (0, 0))

    if not game_over:
        alien.draw()
        planeta.draw()

        screen.draw.text(
            "Score: " + str(score),
            (700, 5),
            color="white"
        )

        screen.draw.text(
            "Life: " + str(life),
            (600, 5),
            color="white"
        )
    else:
        screen.draw.text(
            "GAME OVER \nFinal score: " + str(score),
            (WIDTH/2, HEIGHT/2),
            color="white"
        )

def update():
    global score, life, game_over

    planeta_pos()
    move_alien()

    #collide
    planeta_collide_alien = planeta.colliderect(alien)

    if planeta_collide_alien:
        score += 1
        planeta.pos = (randint(0, 800), -10)

    if life == 0:
        game_over = True

def planeta_pos():
    global life

    planeta.y += 2
    if planeta.y > HEIGHT:
        planeta.y = 0
        planeta.pos = (randint(0, 800), -10)
        life -= 1

def move_alien():
    if keyboard.left:
        alien.x -= 2
    elif keyboard.right:
        alien.x += 2

pgzrun.go()
#BG: rawpixel.com/Freepik

'''
TODO:
- sound
- add more planets (list)
'''