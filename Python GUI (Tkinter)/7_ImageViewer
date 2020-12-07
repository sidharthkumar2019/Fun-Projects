from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Icons, Images, Exit button')
root.iconbitmap('D:/Python GUI (Tkinter)/test.ico.ico')

my_img = ImageTk.PhotoImage(Image.open("Doge.jpeg"))
my_label = Label(image = my_img,padx=10,pady=10)
my_label.pack()

button_quit = Button(root,padx=30,pady=30,text='I quit!!!', command=root.quit)
button_quit.pack()
root.mainloop()
