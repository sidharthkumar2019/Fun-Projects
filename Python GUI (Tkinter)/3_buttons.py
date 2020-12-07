from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text = 'click..')
    myLabel.pack()

myButton = Button(text = 'click me',padx=50,pady=40,command=myClick,fg='black',bg='green')
myButton.pack()

root.mainloop()
