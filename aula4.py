import pgzrun
from pgzhelper import  *
from random import randint

WIDTH = 800
HEIGHT = 600

frog = Actor("frog_1")
frog.pos = (WIDTH/2, HEIGHT-30)
frog.scale = 2
frog.images = ["frog_1", "frog_2"]
frog.fps = 15

box = Actor("box")
box.pos = (randint(0, 800), -10)
box.scale = 1.5

score = 0
life = 5
game_over = False

def draw():
    screen.blit("forest", (0, -150))

    if not game_over:
        frog.draw()
        box.draw()

        screen.draw.text(
            "Score: " + str(score),
            (650, 5),
            fontname="pixellari",
            color="white"
        )

        screen.draw.text(
            "Life: " + str(life),
            (550, 5),
            fontname="pixellari",
            color="white"
        )
    else:
        screen.draw.text(
            "GAME OVER \nFinal score: " + str(score),
            midtop=(400, 100),
            fontname="pixellari",
            color="white"
        )

def update():
    global score, life, game_over

    box_pos()
    move_frog()

    box_collide_frog = box.colliderect(frog)

    if box_collide_frog and not game_over:
        score += 1
        box.pos = (randint(0, 800), -10)
        sounds.box_collide.play()

    if life == 0:
        game_over = True

def box_pos():
    global life

    box.y += 3
    if box.y > HEIGHT and not game_over:
        box.y = 0
        box.pos = (randint(0, 800), -10)
        sounds.box_missed.play()
        life -= 1

def move_frog():
    if keyboard.left:
        frog.animate()
        frog.x -= 2
        frog.flip_x = True
        if keyboard.space:
            frog.x -= 3
    elif keyboard.right:
        frog.animate()
        frog.x += 2
        frog.flip_x = False
        if keyboard.space:
            frog.x += 3

music.play("night_theme")
music.set_volume(0.5)

pgzrun.go()