import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT=650

#dimensions of rect = x,y,w,h
marquee_box = Rect(0,0,880,80)
question_box = Rect(20,100,650,150)
timer_box = Rect(700,100,150,150)
answer_box1 = Rect(20,270,300,150)
answer_box2 = Rect(370,270,300,150)
answer_box3 = Rect(20,450,300,150)
answer_box4 = Rect(370,450,300,150)
skip_box = Rect(700,270,150,330)

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
score = 0
time_left=10
question_file_name="questions.txt"
marquee_message=""
is_game_over = False
questions=[]
question_count = 0
question_index = 0


def draw():
    screen.clear()
    screen.fill(color="hotpink")
    screen.draw.filled_rect(marquee_box,"pink")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(timer_box,"pink")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"violet")

    screen.draw.filled_rect(skip_box,"black")

    marquee_message = "Welcome to Quiz Master..."
    marquee_message = marquee_message + f"Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message,marquee_box,color="black")
    screen.draw.textbox(str(time_left),timer_box,color="black",shadow=(0.5,0.5),scolor="pink")
    screen.draw.textbox("skip",skip_box,color="pink",angle=-90)

    screen.draw.textbox(question[0].strip(),question_box,color="white",shadow=(0.5,0.5),scolor="pink")

    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="black")
        index=index+1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x -=2
    if marquee_box.right < 0:
        marquee_box.left- WIDTH

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count +=1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index +=1
        if skip_box.collidepoint(pos):
            skip_question()

def correct_answer():
    global score,question,time_left,questions
    score+=1
    if questions:
        question=read_next_question()
        time_left=10
    else:
        game_over()

def game_over():
    global question,time_left,is_game_over
    message=f"Game over!\n You got {score} questions correct!!"
    question = [message,"-","-","-","-",5]
    time_left = 0
    is_game_over = True

def update_time_left():
    global time_left
    if time_left:
        time_left -=1
    else:
        game_over()

read_question_file()
question=read_next_question()
clock.schedule_interval(update_time_left,1)

pgzrun.go()
