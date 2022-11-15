#Mu Editor - Pygame Zero mode
import pgzrun
from pgzhelper import  *
from random import randint

bg_color = "#F5BB6B"
green_color = "#72a11d"
pink_color = "#ea71bd"

score_frog = 0
score_pink = 0
game_over = False
game_time = 15

trophy = Actor('trophy')
frog = Actor('frog_idle')
pink = Actor('pink_idle')

trophy.scale = 1.5
frog.scale = 2
pink.scale = 2

trophy.x = 400
trophy.y = 300

def draw():
    global bg_color
    screen.fill(bg_color)
    screen.draw.text("FROG: " + str(score_frog), color=green_color, topleft=(10, 10))
    screen.draw.text("PINK: " + str(score_pink), color=pink_color, topleft=(10, 30))
    screen.draw.text("TIME: " + str(game_time), color="white", midtop=(400, 10))

    trophy.draw()
    frog.draw()
    pink.draw()

    if game_time == 4:
        bg_color = "#f5936b"

    if game_over:
        screen.fill("#D0D0D0")
        screen.draw.text("GAME OVER", color="white", midtop=(400, 10))
        screen.draw.text("FROG: " + str(score_frog),
                         color=green_color,
                         midtop=(400, 50),
                         fontsize=30)

        screen.draw.text("PINK: " + str(score_pink),
                         color=pink_color,
                         midtop=(400, 80),
                         fontsize=30)

def update():
    global score_frog, score_pink, game_time
    move_frog()
    move_pink()

    #Frog and Pink touch the Trophy
    frog_touchs_trophy = frog.collide_pixel(trophy)
    pink_touchs_trophy = pink.collide_pixel(trophy)

    if frog_touchs_trophy:
        score_frog += 1
        random_trophy()
    elif pink_touchs_trophy:
        score_pink += 1
        random_trophy()

def time_up():
    global game_over
    game_over = True

def countdown():
    global game_time
    game_time -= 1

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

def move_pink():
    if keyboard.a:
        pink.x -= 2
    elif keyboard.d:
        pink.x += 2
    elif keyboard.w:
        pink.y -= 2
    elif keyboard.s:
        pink.y += 2

#set time = 15s
clock.schedule(time_up, 15)
#set countdown
clock.schedule_interval(countdown, 1)
pgzrun.go()
