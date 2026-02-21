import pgzrun
from random import randint

WIDTH = 600
HIEGHT = 500

oggy=Actor("oggy")
oggy.pos=100,100
score = 0
game_over=False

ch=Actor("ch")
ch.pos =50,50

def draw():
    screen.blit("house",(0,0))
    oggy.draw()
    ch.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))

if game_over:
    screen.fill("black")
    screen.draw.text("Time's up!Your final score:"+str(score),midtop=(300,10),frontsize=40,color="violet")

def place_ch():
    ch.x = randint(50,WIDTH-50)
    ch.y = randint(50,HIEGHT-50)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        oggy.x=oggy.x-2
    if keyboard.right:
        oggy.x=oggy.x+2
    if keyboard.up:
        oggy.y=oggy.y-2
    if keyboard.down:
        oggy.y=oggy.y+2

    ch_collected=oggy.colliderect(ch)
    
    if ch_collected:
        score=score+10
        place_ch()

clock.schedule(time_up,60.0)

pgzrun.go()
