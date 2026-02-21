import pgzrun
import random

WIDTH  = 840
HEIGHT = 600
CENTER = (400,300)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["battery","bottle","chips","paperbags","plasticbag"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items,current_level,game_complete,game_over
    screen.clear()
    screen.blit("recycle",(0,0))
    if game_over:
        display_message("Game Over","Try again..")
    elif game_complete:
        display_message("You Won","Well done..")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paperbags"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
    
def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item=Actor(option)
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH /number_of_gaps   
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):  #enumerate is a built function that helps run the loop from the list
        new_x_pos = (index+1)* gap_size   #gives the gap position
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration =      START_SPEED - current_level
        item.anchor = ("center","bottom") #anchor = how i want it to flow
        animation = animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation) #adds the animation

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global item,current_level
    for item in items:
        if item.collidepoint(pos):
            if"paperbags"in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global items,current_level,animations,game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
            
def display_message(heading_text,sub_heading_text):
    screen.draw.text(heading_text,fontsize=60,center = CENTER,color = "black")
    screen.draw.text(sub_heading_text,fontsize=30,center = (400,330),color = "black")

pgzrun.go()

