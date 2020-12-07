from tkinter import *

root = Tk()

e = Entry(root, width=50, fg='black', bg='yellow')
e.pack()
e.insert(0,'Username')

def myClick():
    hello = '_Hello_'+e.get()
    myLabel = Label(root,text = hello)
    myLabel.pack()

myButton = Button(text = 'click me',padx=30,pady=20,command=myClick,fg='black',bg='green')
myButton.pack()

root.mainloop()
