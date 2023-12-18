"""
    Doing some pythone pssssstt.......(snake sound) 
    of course when it comes to first time learning python
    you gonna have to do the snake game YEAH BOY.
"""

import keyboard
import os
import datetime
import random

BOARD = []
column = 40
row = 40

SNAKE = {
    "x": 0,
    "y": 0,
    "add_x": 1,
    "add_y": 0,
    "tails": []
}

FOOD = {
    "x": 0,
    "y": 0
}

milli = float(0)
fps = 0.2

game_over = False

score = 0

def create_board():
    for y in range(0,column):
        row_item = []
        for x in range(0,row):
            if (x == 0 or y == 0 or x == row - 1 or y == column - 1):
                row_item.append("#")
            else:
                row_item.append(" ")
        BOARD.append(row_item)

def update_board():
    for y in range(0,len(BOARD)):
        for x in range(0,len(BOARD[y])):
            if (x == 0 or y == 0 or x == row - 1 or y == column - 1):
                BOARD[y][x] = "#"
            else:
                BOARD[y][x] = " "

def draw_board():
    for y in range(0,len(BOARD)):
        row_item = "";
        for x in range(0,len(BOARD[y])):
            row_item += BOARD[y][x]
        print(row_item)
        
#def draw_snake():
#    # draw the snake by updating the board at [y][x]
#    x = SNAKE["x"]
#    y = SNAKE["y"]
#    BOARD[y][x] = "@"
#
#def draw_food():
#    # the same as draw_snake
#    x = FOOD["x"]
#    y = FOOD["y"]
#    BOARD[y][x] = "*"

def draw_by_coord(object,symbol):
    x = object["x"]
    y = object["y"]
    BOARD[y][x] = symbol

def update_tails():
    tails = SNAKE["tails"]
    for x in range(0,len(tails)):
        i = len(tails) - 1- x
        prev_tail = tails[i - 1]
        tails[i] = {
            "x": prev_tail["x"],
            "y": prev_tail["y"]
        }

    
def draw_snake():
    symbol = "0"
    tails = SNAKE["tails"] 

    for i in range(1,len(tails)):
        draw_by_coord(tails[i],symbol)
        
    # draw head
    draw_by_coord(tails[0],"@")
        
def update_snake():
    # update X and Y from addX and addY 
    prev_x = SNAKE["x"]
    new_x = prev_x + SNAKE["add_x"]
    edge_x = row - 1

    prev_y = SNAKE["y"]
    new_y = prev_y + SNAKE["add_y"]
    edge_y = column - 1
    
    # update the tails position before updating the snake position
    update_tails()

    # update snake position
    SNAKE["x"] = new_x
    SNAKE["y"] = new_y

    # check if the snake collide with wall
    if SNAKE["x"] == edge_x:
        SNAKE["x"] = 1
    elif SNAKE["x"] == 0:
        SNAKE["x"] = edge_x

    if SNAKE["y"] == edge_y:
        SNAKE["y"] = 1
    elif SNAKE["y"] == 0:
        SNAKE["y"] = edge_y

    SNAKE["tails"][0]["x"] = SNAKE["x"]
    SNAKE["tails"][0]["y"] = SNAKE["y"]

def add_tail():
    global tails

    tails = SNAKE["tails"]
    last_tail = tails[len(tails) - 1]

    x = SNAKE["x"]
    y = SNAKE["y"]
    if last_tail in tails:
      x = last_tail["x"]
      y = last_tail["y"]
      
    tails.append({
       "x": x,
       "y": y
    })
    

def collission(first,second):
    f_x = first["x"]
    f_y = first["y"]

    s_x = second["x"]
    s_y = second["y"]

    return (f_x == s_x and f_y == s_y)

    
def randomize_position(object):
    object["x"] = random.randint(1,row - 2)
    object["y"] = random.randint(1,column - 2)


def add_logic(): 
    global score
    global game_over

    update_snake()

    if collission(SNAKE,FOOD):
        score += 1
        randomize_position(FOOD)
        add_tail()

    tails = SNAKE["tails"]
    print(tails)
    for i in range(2,len(tails)):
        tail = tails[i]
        print(tail)
        if collission(SNAKE,tail):
            game_over = True


def init():
    create_board()
    randomize_position(SNAKE)
    randomize_position(FOOD)

    SNAKE["tails"].append({
        "x": SNAKE["x"],
        "y": SNAKE["y"]
    })


def clear_screen():
    # clear the terminal texts
    os.system("cls")

def add_controlls():
    add_x = SNAKE["add_x"]
    add_y = SNAKE["add_y"]

    # listen for key pressed, then update addX and addY by the key that is pressed
    if keyboard.is_pressed("d") and add_x != -1:
       SNAKE["add_x"] = 1
       SNAKE["add_y"] = 0
    elif keyboard.is_pressed("a") and add_x != 1:
       SNAKE["add_x"] = -1
       SNAKE["add_y"] = 0
    
    if keyboard.is_pressed("w") and add_y != 1:
       SNAKE["add_y"] = -1
       SNAKE["add_x"] = 0
    elif keyboard.is_pressed("s") and add_y != -1:
       SNAKE["add_y"] = 1
       SNAKE["add_x"] = 0

def add_display():
    print("Score: ",score * 1000)
    

def start_game():
    # start the game
    init()
    global milli
    while True:
        if game_over:
            print("GAME OVER!")
            break

        # draw the game depend on fps
        if ((milli / 1000) < (1000/fps)):
            now = datetime.datetime.now()
            milli = milli + float(int(now.strftime("%f")) / 1000)
        else: 
            milli = 0
            clear_screen()
            update_board()
            add_display()
            add_logic()
            draw_snake()
            add_controlls()
            draw_by_coord(FOOD,"*")
            draw_board()

start_game()
