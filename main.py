from tkinter import *;
import random

def next_turn(row,col):
    global player;

    if buttons[row][col]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][col]['text'] = player;
            if check_winner() is False:
                player = players[1];
                label.config(text=(player + " turn"));
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"));
            elif check_winner() == "Tie":
                label.config(text=("Tie!"));
        else:
            buttons[row][col]['text'] = player;
            if check_winner() is False:
                player = players[0];
                label.config(text=(player + " turn"));
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"));
            elif check_winner() == "Tie":
                label.config(text=("Tie!"));


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True;
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return True;
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True;
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True;
    elif empty_spaces() is False:
        return "Tie";
    else:
        return False;
    

def empty_spaces():
    spaces = 9;

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces -= 1;
    
    if spaces == 0:
        return False;
    else:
        return True;

def new_game():
    global player;

    player = random.choice(players);
    label.config(text=(player + " turn"));

    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = "";

mywin = Tk();
mywin.title("Tic Tac Toe");

players = ["x","o"];
player = random.choice(players);
label = Label(text=(player + " turn"),
              font=('consolas',40));
label.pack();

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]];
restart_btn = Button(text="Restart",
                     font=('consolas',20),
                     command=new_game);
restart_btn.pack();

frame = Frame(mywin);
frame.pack();

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame,
                                   text="",
                                   font=('consolas',40),
                                   width=4,
                                   height=1,
                                   command=lambda row=row,col=col:next_turn(row,col));
        buttons[row][col].grid(row=row,column=col);

mywin.mainloop();