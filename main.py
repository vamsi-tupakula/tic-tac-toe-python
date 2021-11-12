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
    pass;

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
                     font=('consolas',20));
restart_btn.pack();

frame = Frame(mywin);
frame.pack();

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame,
                                   text="",
                                   font=('consolas',30),
                                   width=6,
                                   height=2);
        buttons[row][col].grid(row=row,column=col);

mywin.mainloop();