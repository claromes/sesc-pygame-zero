#mu editor mode
import pgzrun

virtual = Actor('virtual_idle') #/images/virtual_idle.png
virtual.pos = 300, 250

WIDTH = 400
HEIGHT = 300

def draw():
    screen.clear()
    screen.fill((75, 0, 130))

    screen.draw.text('Virtual Guy Game', topleft=(5,5))
    screen.draw.circle((225, 175), 30, 'white')
    screen.draw.rect(Rect(100, 50, 60, 60), 'white')
    virtual.draw()

pgzrun.go() #run the code