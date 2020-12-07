from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('_Photo_Roto_')
root.iconbitmap('D:/Python GUI (Tkinter)/test.ico.ico')

my_img1 = ImageTk.PhotoImage(Image.open("Images/1.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/4.jpg"))

my_list = [my_img1,my_img2,my_img3,my_img4]

status = Label(root,text='Image 1 of'+str(len(my_list)),bd=1,relief=SUNKEN,anchor=E)
my_label = Label(image = my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def foreward(img_ind):
    status = Label(root,text='Image '+ str(img_ind+1) +' of'+str(len(my_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

    global button_back
    global button_foreward
    global my_label

    my_label.grid_forget() # To prevent the current image from overlapping with the next image
    my_label = Label(image = my_list[img_ind])
    my_label.grid(row=0,column=0,columnspan=3)

    if img_ind == len(my_list)-1:
        button_foreward = Button(root,text='>>',state = DISABLED)
    else:
        button_foreward = Button(root,text='>>',command=lambda: foreward(img_ind+1))
    button_back = Button(root,text='<<',command=lambda: back(img_ind-1))

    button_back.grid(row=1,column=0)
    button_foreward.grid(row=1,column=2)

def back(img_ind):
    status = Label(root,text='Image '+ str(img_ind+1) +' of'+str(len(my_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

    global button_back
    global button_foreward
    global my_label

    my_label.grid_forget() # To prevent the current image from overlapping with the next image
    my_label = Label(image = my_list[img_ind])
    my_label.grid(row=0,column=0,columnspan=3)

    if img_ind == 0:
        button_back = Button(root,text='<<',state=DISABLED)
    else:
        button_back = Button(root,text='<<',command=lambda: back(img_ind-1))
    button_foreward = Button(root,text='>>',command=lambda: foreward(img_ind+1))

    button_back.grid(row=1,column=0)
    button_foreward.grid(row=1,column=2)


button_back = Button(root,text='<<',command=DISABLED)
button_exit = Button(root,text='Exit',command=root.quit)
button_foreward = Button(root,text='>>',command=lambda: foreward(1))

button_back.grid(row=1,column=0)
button_foreward.grid(row=1,column=2)
button_exit.grid(row=1,column=1,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
