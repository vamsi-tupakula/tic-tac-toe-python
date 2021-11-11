from tkinter import *;
import random

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