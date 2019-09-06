import tkinter as tk
from tkinter import *
## Method initiation ##
from tkinter import Frame
## Reference to library##
r = tk.Tk ( )
## Title name ##
r.title ('Python open source tool')
## Reference to library##
F = Frame (r)
## Menu Option Method ##
menu = Menu(r)
r.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=r.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='System setting', menu=helpmenu)
helpmenu.add_command(label='1')
menu.add_cascade(label='Task info', menu=helpmenu)
helpmenu.add_command(label='2')
menu.add_cascade(label='About STAT', menu=helpmenu)
helpmenu.add_command(label='3')
## List box for left side ##
Lb = Listbox ( F, width = 60 , height = 40 , borderwidth = 2)
Lb.pack ( side = LEFT )
## scrollbar method ##
scroll1 = Scrollbar ( F )
scroll1.pack ( side = RIGHT , fill = Y )
## List box with scroll on right side ##
Lb1 = Listbox ( F , width = 40 , height = 10 , borderwidth = 2 ,
                yscrollcommand = scroll1.set )
for i in range ( 1 , 100 ) :
    Lb1.insert ( END , "        " )
Lb1.pack ( side = RIGHT , fill = BOTH )
scroll1.config ( command = Lb1.yview )
## Activate ##
F.pack ( )
r.geometry ( )
r.mainloop ( )
