from tkinter import *

root = Tk()
root.config(bg = 'black')

for i in range(4):
    but = Button(root, text = str(i), bg = 'yellow', width = 20,
                 height = 10)
    but.grid(row = 0, column = i)

for i in range(4):
    but = Button(root, text = str(i+1), bg = 'red', width = 20,
                 height = 10)
    but.grid(row = 1, column = i)

for i in range(4):
    but = Button(root, text = str(i+2), bg = 'cyan', width = 20,
                 height = 10)
    but.grid(row = 2, column = i)


root.mainloop()