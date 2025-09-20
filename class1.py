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

score = 0
def on_mouse_down(pos):
    global message
    global score
    #score = 0
    if ball.collidepoint(pos):
        message="Good shot"
        score = score + 1
        print(score)
        place_ball()
    else:
        message="You missed"
        score = score - 1
        print(score)
    
place_ball()
pgzrun.go()