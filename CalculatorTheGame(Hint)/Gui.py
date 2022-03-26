# !/usr/bin/python3
from tkinter import *
import os

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

################################################
point_Label=Label(frame,text = "point",font=('Times',20))
point_Label.pack()
point_Entry = Entry(frame,bg='cyan')
point_Entry.pack()
########################
goal_Label=Label(frame,text = "goal",font=('Times',20))
goal_Label.pack()
goal_Entry = Entry(frame,bg='cyan')
goal_Entry.pack()
########################
MOVES_Label=Label(frame, text = "moves",font=('Times',20))
MOVES_Label.pack()
MOVES_Entry = Entry(frame,bg='cyan')
MOVES_Entry.pack()
########################
NUMBER_Label=Label(frame,text = "numbers",font=('Times',20))
NUMBER_Label.pack()
NUMBER_Entry = Entry(frame,bg='cyan',font=('Times',20))
NUMBER_Entry.pack()
############################################

def FOOO():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    os.system("a.exe {p} {g} {M} {N}".format(p=point_Entry.get(),g=goal_Entry.get(),M=MOVES_Entry.get(),N=NUMBER_Entry.get()))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
   
Button(frame,text='Show',bg='red',width=30,bd=3,command=FOOO ).pack()
root.mainloop()