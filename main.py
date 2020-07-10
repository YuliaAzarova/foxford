from tkinter import *
from random import *
from time import *


root = Tk()
root.geometry('700x400')
root.config(bg = 'black')
root.title('Мемори')

first = True

def Click(event):
    t = event.widget
    x = t.grid_info()['column']
    global first
    global prev
    if first == True:
        buttons[x].config(text=sumbols[x])
        first = False
        prev = x
    else:
        if x == prev:
            buttons[x].config(text = '')
            first = True
        else:
            buttons[x].config(text = sumbols[x])
            buttons[x].update_idletasks()
            if sumbols[x] == sumbols[prev]:
                buttons[x]
                buttons[prev].config(bg = 'red')
                buttons[x].unbind('<Button-1>')
                buttons[prev].unbind('<Button-1>')
            else:
                sleep(1)
                buttons[x]. config(text = '')
                buttons[prev]. config(text = '')
            first = True

buttons = []
sumbols = ['\u2603', '\u2603', '\u2604', '\u2604', '\u2614',
           '\u2614', '\u2618', '\u2618', '\u2620', '\u2620',
           '\u263A', '\u263A']

shuffle(sumbols)

for i in range(12):
    but = Button(root, bg = 'red', fg = 'dark blue', width = '5',
                 height = '4')
    buttons.append(but)
    but.bind('<Button-1>', Click)
    but.grid(row = 0, column = i, padx = 5)


root.mainloop()