import pgzrun
import random

WIDTH = 800
HIEGHT = 650
CENTER = (400,300)
items = []
score = 0

game_over  = False
game_complete = False
player = Actor("spaceship")
player.pos = (500,300)

bullets = []
astronuts = []
aliens = []
bullet = Actor("bullet")
bullet.pos = (-100,-100)
bullet_active = False


for i in range(5):
    alien = Actor("alien")
    alien.pos = random.randint(50,750),random.randint(50,200)
    aliens.append(alien)
for i in range(3):
    astronut = Actor("astronut")
    astronut.pos = random.randint(50,750),random.randint(50,200)
    astronuts.append(astronut)

def draw():
    screen.clear()
    screen.fill("black")
    if game_over:
        screen.draw.text("GAME OVER",center = (400,300), fontsize = 60, color ="red")
        screen.draw.text("Score: " + str(score), center=(400,360), frontsize=40)
        return
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for alien in aliens:
        alien.draw()
    for astronut in astronuts:
        astronut.draw()
    
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
        for alien in aliens:
            if bullet.colliderect(alien):
                bullets.remove(alien)
                score +=1
                break
    for bullet in bullets:
        for astro in astronuts:
            if bullet.coliderect(astro):
                game_over = True

def on_key_down(key):
    if key == keys.SPACE and not game_over:
        bullet = Actor("bullet")
        bullet.pos = player.pos
        bullets.append(bullet)

pgzrun.go()