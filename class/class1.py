import pgzrun
from random import randint

TITLE = "Good Shot"

WIDTH = 500
HEIGHT = 500

message = ""

ball = Actor("ball")

def draw():
    screen.clear()
    screen.fill("cyan")
    ball.draw()
    screen.draw.text(message,center = (400,10),fontsize=30)

def place_ball():
    ball.x=randint(50,WIDTH-50)
    ball.y=randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if ball.collidepoint(pos):
        message="Good shot"
        place_ball()
    else:
        message="You missed"

place_ball()
pgzrun.go()