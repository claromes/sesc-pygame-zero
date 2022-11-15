'''Flappy Game by Claromes
Assets by Pixel Frog, Zacchary Dempsey-Plante, ObsydianX and SVL
Helper by A Posteriori
'''

import pgzrun
from pgzhelper import  *
from random import randint

WIDTH = 800
HEIGHT = 600

up = False
game_over = False
life = 5
score = 0
level = 1
appearing = False

mask = Actor("mask_fall")
mask.pos = (WIDTH / 2, HEIGHT / 2)
mask.scale = 2

head = Actor("spike_head")
head.pos = randint(800, 1000), randint(50, 100)
head.scale = 2
head.images = ["spike_head", "spike_head_closed"]
head.fps = 1

ball = Actor("spike_ball")
ball.pos = randint(800, 1200), randint(400, 450)
ball.scale = 2

rock = Actor("rock_head")
rock.pos = randint(800, 1300), randint(200, 300)
rock.scale = 2
rock.images = ["rock_head_hit_1", "rock_head_hit_2", "rock_head_hit_3", "rock_head", "rock_head_hit_4", "rock_head_hit_5", "rock_head_hit_6"]
rock.fps = 12

saw = Actor("saw")
saw.pos = -20, randint(450, 580)

fire_list = []
fire_x = [25, 735]
for i in range(2):
    fire = Actor("fire_3")
    fire.pos = 25 + fire_x[i], 580
    fire.scale = 1.5
    fire.images = ["fire_3", "fire_2", "fire_1"]
    fire.fps = 10
    fire_list.append(fire)

app = Actor("appearing_4")
app.pos = (WIDTH / 4, HEIGHT / 2)
app.images = ["appearing_4", "appearing_3", "appearing_2", "appearing_1"]
app.fps = 12

trophy = Actor("trophy")
trophy.pos = midtop=(400, 300)
trophy.scale = 1.5

def draw():
    if not game_over:
        screen.blit("background", (0, 0))
        screen.draw.text("Level: " + str(level), midtop=(250, 5), fontname="pixellari", color="white")
        screen.draw.text("Score: " + str(score), midtop=(400, 5), fontname="pixellari", color="white")
        screen.draw.text("Life: " + str(life), midtop=(550, 5), fontname="pixellari", color="white")

        mask.draw()
        head.draw()
        ball.draw()
        rock.draw()
        saw.draw()

        for fire in fire_list:
            fire.draw()

        if appearing:
            app.draw()
    else:
        screen.fill("#9fcc98")
        screen.draw.text("GAME OVER \nFinal score: " + str(score),
                        midtop=(400, 5),
                        fontname="pixellari",
                        color="white")
        trophy.draw()

def update():
    global life, game_over, appearing

    mask_pos()
    ball_pos()

    for fire in fire_list:
        fire.animate()

    if level >= 2:
        head_pos()
        head.animate()
    if level >= 3:
        rock_pos()
        rock.animate()
    if level >= 4:
        saw_pos()

    if score == 3 or score == 7 or score == 11:
        sounds.game_level.play()

    mask_collide_head = head.collide_pixel(mask)
    mask_collide_ball = ball.collide_pixel(mask)
    mask_collide_rock = rock.collide_pixel(mask)
    mask_collide_saw = saw.collide_pixel(mask)

    if mask_collide_head or mask_collide_ball or mask_collide_rock or mask_collide_saw:
        sounds.mask_collide.play()
        life -= 1
        mask_pos_after_collide()

    if appearing:
        app.animate()
        app.pos = mask.pos
        if mask.y == 310:
            app.scale = 0
            appearing = False

    if life == 0:
        game_over = True

    levels()

def on_mouse_down():
    global up

    if not appearing:
        up = True
        mask.y -= 30
        mask.image = "mask_jump"

def on_mouse_up():
    global up
    up = False
    mask.image = "mask_fall"

def head_pos():
    global score
    if head.x > -50:
        head.x -= 2
    else:
        head.pos = randint(800, 1000), randint(50, 100)
        if not game_over:
            score += 1

def ball_pos():
    global score
    if ball.x > -50:
        ball.x -= 3
        ball.angle += 6
    else:
        ball.pos = randint(800, 1200), randint(400, 550)
        if not game_over:
            score += 1

def rock_pos():
    global score
    if rock.x > -50:
        rock.x -= 2
    else:
        rock.pos = randint(800, 1300), randint(200, 300)
        if not game_over:
            score += 1

def mask_pos():
    global game_over
    #gravity
    if not up:
        mask.y += 1

    if mask.top < 0 or mask.bottom > 600:
        game_over = True

def saw_pos():
    global score
    if saw.x < 850:
        saw.angle -= 5
        saw.move_in_direction(3)
    else:
        saw.pos = -10,  randint(50, 580)
        if not game_over:
            score += 1

def mask_pos_after_collide():
    global appearing

    appearing = True
    app.scale = 1.5

    mask.x = randint(50, 500)
    mask.y = HEIGHT / 2

def levels():
    global level

    if score >= 3 and score <= 6:
        level = 2
    elif score >= 7 and score <= 10:
        level = 3
    elif score > 10:
        level = 4

music.play("cave_theme")
music.set_volume(0.5)

hide_mouse()

pgzrun.go()