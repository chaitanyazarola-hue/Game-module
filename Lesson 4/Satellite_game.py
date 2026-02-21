import pgzrun   #imports the pgzrun module
from random import randint  #imports random module
from time import time #imports time module

WIDTH = 800  #sets the width of the screen
HEIGHT =480  #sets the height of the screen

satellites = []  
lines = []
number_of_satellite=8   #sets the number of setalite

next_satellite=0

start_time=0 # the start and end time is wrriten
total_time=0
end_time=0

def create_satellites():  
    global start_time     #a function is created as create_satellites
    for count in range(0,number_of_satellite):
        satellite=Actor("satellite")
        x=randint(50,750)
        y=randint(50,450)
        satellite.pos=x,y
        satellites.append(satellite)
    start_time=time()

def draw():
    global total_time
    screen.blit("bg",(0,0)) #another function is created as draw
    number=1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number=number+1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

    if next_satellite < number_of_satellite:
        total_time=time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_satellite,lines

    if next_satellite < number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite=next_satellite+1
        else:
            lines=[]
            next_satellite=0

create_satellites()
pgzrun.go()



