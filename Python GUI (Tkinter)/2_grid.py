from tkinter import *

root = Tk()
# creating a label widget
myLabel_1 = Label(root, text = 'Hello world!')
myLabel_2 = Label(root, text = 'I am learning Tkinter')
myLabel_3 = Label(root, text = '______')
# showing it on the screen
myLabel_1.grid(row=0, column = 0)
myLabel_2.grid(row=1, column = 2)
myLabel_3.grid(row=1,column=1)
root.mainloop()
