from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title('Adding Frame')
#frame = LabelFrame(root, text="this is a frame", padx= 50, pady = 50)
#frame.pack()
#tt = Button(frame, text="Exit",padx=10,pady=10)
#tt.grid(row=0, column=0)
Modes = [("Cheese","Cheese"), ("Pepperoni","Pepperoni"),
         ("Mushroom","Mushroom"),("Onion","Onion"),("Oregano","Oregano")]
r = StringVar()
r.set("Cheese")
for text, mode in Modes:
    Radiobutton(root, text=text, variable=r,value=mode).pack(anchor=W)
def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:click(r.get())).pack()

#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:click(r.get())).pack()
myLabel = Label(root,text=r.get())
myLabel.pack()
myButton = Button(root,text="Click me", command=lambda:click(r.get()))
myButton.pack()
mainloop()
