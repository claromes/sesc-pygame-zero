#mu editor mode
import pgzrun

alien = Actor('alien') #/images/alien.png
alien.pos = 200, 250

WIDTH = 400
HEIGHT = 300

def draw():
    screen.clear()
    screen.fill((50,0,240))

    screen.draw.text('Alien Game', topleft=(5,5))
    screen.draw.circle((200, 150), 30, 'white')
    alien.draw()

pgzrun.go() #run the code
