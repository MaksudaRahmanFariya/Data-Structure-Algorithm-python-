from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title('Learn to code')
#root.iconbitmap('C:\Users\Tarning\Documents\owl.png')
#but_qu = Button(root,text="Exit",command=root.quit)
my_image1 = ImageTk.PhotoImage(Image.open(r"black-cat.png"))
#my_image2 = ImageTk.PhotoImage(Image.open(r"halloween-witch-cap.png"))
#my_image3 = ImageTk.PhotoImage(Image.open(r"monstera.png"))
#my_image4 = ImageTk.PhotoImage(Image.open(r"dracula.png"))
my_image5 = ImageTk.PhotoImage(Image.open(r"owl.png"))
my_image3 = ImageTk.PhotoImage(Image.open(r"heart_1.png"))
my_image6 = ImageTk.PhotoImage(Image.open(r"heart.png"))
image_list = [my_image1, my_image3,my_image5,my_image6]
# image label
my_l = Label(root,image=my_image1)
my_l.grid(row=0,column=0,columnspan=3)
def forward(image_number):
    global my_l
    global forward
    global back
    my_l.grid_forget()
    my_l = Label(root, image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number == len(image_list):
        button_forward = Button(root, text=">>",state=DISABLED)
    my_l.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status = Label(root, text = "Image " + str(image_number) + " of" + str(len(image_list)), bd = 1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky = W+E)

def back(image_number):
    global my_l
    global forward
    global back
    my_l.grid_forget()
    my_l = Label(root,image = image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<",state=DISABLED)
    my_l.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status = Label(root, text = "Image " + str(image_number) + " of" + str(len(image_list)), bd = 1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky = W+E)





button_back = Button(root,text="<<",command=lambda:back(1), state=DISABLED)
button_forward = Button(root, text=">>",command=lambda:forward(2))
but_qu = Button(root,text="Exit",command=root.quit)
button_back.grid(row=1,column=0)
but_qu.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)

#but_qu.pack()
root.mainloop()