#add score + game over screen
import pgzrun  #mu editor mode
from random import randint  #random int numbers

BG_COLOR = "#9469b5"

score = 0
game_over = False

rob = Actor('robo')
dot = Actor('dot')
giga = Actor('giga')

rob.x = 400
rob.y = 300

def draw():
    screen.fill(BG_COLOR)
    screen.draw.text("Pontos: " + str(score), color="yellow", topleft=(10, 10))

    rob.draw()
    dot.draw()
    giga.draw()

    if game_over:
        screen.fill("black")
        screen.draw.text("Total de Pontos: " + str(score),
                         color="white",
                         topleft=(10, 10),
                         fontsize=60)

def update():
    global score
    move_dot()
    move_giga()

    #Dot touchs Rob
    dot_touchs_rob = dot.colliderect(rob)
    giga_touchs_rob = giga.colliderect(rob)

    if dot_touchs_rob or giga_touchs_rob:
        score += 1
        random_rob()

def time_up():
    global game_over
    game_over = True

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

def move_giga():
    if keyboard.A:
        giga.x -= 2
    elif keyboard.D:
        giga.x += 2
    elif keyboard.W:
        giga.y -= 2
    elif keyboard.S:
        giga.y += 2

#set time = 15s
clock.schedule(time_up, 15)
pgzrun.go()  #run the code