import pgzrun
from random import randint

WIDTH = 800
HIEGHT = 500

boy=Actor("boy")
boy.pos=100,100
score = 0
game_over=False

ball=Actor("ball")
ball.pos=100,100

def draw():
    screen.blit("field",(0,0))
    boy.draw()
    ball.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Time's up!Your final score : "+str(score),midtop=(300,10),fontsize=40,color="violet")

def place_ball():
    ball.x = randint(50,WIDTH-50)
    ball.y = randint(50,HIEGHT-50)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        boy.x = boy.x -2
    if keyboard.right:
        boy.x = boy.x +2
    if keyboard.up:
        boy.y = boy.y -2
    if keyboard.down:
        boy.y = boy.y +2

    ball_collected=boy.colliderect(ball)

    if ball_collected:
        score=score+10
        place_ball()

clock.schedule(time_up,60.0)

pgzrun.go()