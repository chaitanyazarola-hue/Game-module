import pgzrun
from random import randint
from time import time

WIDTH = 750
HEIGHT = 500

potions = []
number_of_potion = 10
next_potion = 0

def creat_potion():
    for i in range (0,number_of_potion):
        potion =Actor("potion")
        x =randint(50,750)
        y = randint(50,500)
        potion.pos=x,y
        potions.append(potion)

def draw():
    screen.blit("enchanted_forest",(0,0))
    for i in potions:
        i.draw()

def update():
    pass

creat_potion()
pgzrun.go()
