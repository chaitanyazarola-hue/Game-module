import pgzrun #imports the run module
import random # imports the random module

WIDTH = 800 #width size is created 
HEIGHT = 650 #Height of the screen is set 
CENTER = (400,300)
items = []
score = 0

game_over  = False
game_complete = False
player = Actor("jet")
player.pos = (500,500)

bullets = []
boys = []
zombies = []
bullet = Actor("bullet")
bullet.pos = (-100,-100)
bullet_active = False


for i in range(5):
    zombie = Actor("zombie")
    zombie.pos = random.randint(50,750),random.randint(50,200)
    zombies.append(zombie)
for i in range(3):
    boy = Actor("boy")
    boy.pos = random.randint(50,750),random.randint(50,200)
    boys.append(boy)

def draw():
    screen.clear()
    screen.fill("black")
    if game_over:
        screen.draw.text("GAME OVER",center = (400,300), fontsize = 60, color ="red")
        screen.draw.text("Score: " + str(score), center=(400,360), fontsize=40)
        return
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for zombie in zombies:
        zombie.draw()
    for boy in boys:
        boy.draw()
    
    screen.draw.text("Score: " +str(score), (10,10), fontsize=30)
    
def update():
    global game_over,score
    if keyboard.left:
        player.x=player.x-5
    if keyboard.right:
        player.x = player.x + 5

    for bullet in bullets:
        bullet.y -= 8

    bullets[:] = [b for b in bullets if b.y > 0]

    for bullet in bullets:
        for zombie in zombies:
            if bullet.colliderect(zombie):
                bullets.remove(bullet)
                zombies.remove(zombie)
                score +=1
                break
    for bullet in bullets:
        for astro in boys:
            if bullet.colliderect(astro):
                game_over = True

def on_key_down(key):
    if key == keys.SPACE and not game_over:
        bullet = Actor("bullet")
        bullet.pos = player.pos
        bullets.append(bullet)

pgzrun.go()