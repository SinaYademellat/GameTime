# !/usr/bin/python3
from tkinter import *
import os

root = Tk()

root.title('input box')

root.resizable(width=False, height=False) # fix -->  window size  :)

#A geometry string is a standard way of describing the size and location of a top-level window on a desktop.
#geometry string has this general form:  'wxh±x±y'  :)
root.geometry('284x267+600+150') 

frame = Frame(root)

#################################### << COLOR >> 

#set window color
BackgroundColorHEX_='#858282'


#################################### << COLOR >> 

frame.configure(bg = BackgroundColorHEX_)

frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

################################################
point_Label=Label(frame,text = "point" , bg = BackgroundColorHEX_ ,font=('Times',20))
point_Label.pack()
point_Entry = Entry(frame,bg='cyan')
point_Entry.pack()
########################
goal_Label=Label(frame,text = "goal", bg = BackgroundColorHEX_ ,font=('Times',20))
goal_Label.pack()
goal_Entry = Entry(frame,bg='cyan')
goal_Entry.pack()
########################
MOVES_Label=Label(frame, text = "moves", bg = BackgroundColorHEX_ ,font=('Times',20))
MOVES_Label.pack()
MOVES_Entry = Entry(frame,bg='cyan')
MOVES_Entry.pack()
########################
NUMBER_Label=Label(frame,text = "numbers", bg = BackgroundColorHEX_ ,font=('Times',20))
NUMBER_Label.pack()
NUMBER_Entry = Entry(frame,bg='cyan',font=('Times',20))
NUMBER_Entry.pack()
############################################

def FOOO():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    os.system("a.exe {p} {g} {M} {N}".format(p=point_Entry.get(),g=goal_Entry.get(),M=MOVES_Entry.get(),N=NUMBER_Entry.get()))
    # < way >
        #1  a.exe ... >> out.txt 'NEXT' py:open() ... :)
        #2  cpp: fstream.... 'NEXT'     py:open() ... :)
        #3  shell: bash script or ...
        #   ?? 
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    # root.destroy()
    newWindow = Toplevel(root)
    lines = []
    with open('sinaYad.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        NUMBER_Label=Label(newWindow,text = line, bg = BackgroundColorHEX_ ,font=('Times',20))
        NUMBER_Label.pack() 

   
Button(frame,text='Show',bg='red',width=30,bd=3,command=FOOO ).pack()

root.mainloop()