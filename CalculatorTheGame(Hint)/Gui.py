# !/usr/bin/python3
from tkinter import *

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
NUMBER_Label=Label(frame,text = "number",font=('Times',20))
NUMBER_Label.pack()
NUMBER_Entry = Entry(frame,bg='cyan')
NUMBER_Entry.pack()

############################################
def FOOO():
    print(point_Entry.get())
    print(goal_Entry.get())
    print(MOVES_Entry.get())
    print(NUMBER_Entry.get())


Button(frame,  text='Show',command=FOOO ).pack()#, command=show_entry_fields)

root.mainloop()