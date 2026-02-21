import pgzrun
from random import randint
from time import time

WIDTH = 750
HEIGHT = 500

splash = []
number_of_splash = 10
next_splash = 0

def creat_splash():
    for i in range (0,number_of_splash):
        splash =Actor("splash")
        x =randint(50,750)
        y = randint(50,500)
        splash.pos=x,y
        splash.append(splash)

def draw():
    screen.blit("desert",(0,0))
    for i in splash:
        i.draw()

def update():
    pass

creat_splash()
pgzrun.go()
