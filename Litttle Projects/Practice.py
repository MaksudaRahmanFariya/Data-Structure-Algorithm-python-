#from tkinter import *                      #Widgets are small, interactive applications that display real-time information on your device, providing quick access to weather, news, calendar events, and more
#root = Tk()                              #creates the main application window           
#Creating a label Widget
#my_label0 = Label(root, text="Hi Bini")  #root means place this label inside the main window.
#my_label1 = Label(root, text="Hi nini")
#invoking into the screen
#my_label.pack()                   #places the label inside the window so it becomes visible
#my_label0.grid(row=0, column = 0)
#my_label1.grid(row = 0, column = 1)
#event loop continuously running                   
#my_label1 = Label(root, text="Hi nini")
#name = Entry(root,width=30)
#name.pack()
#name.insert(0, "Enter Your Name:")
#def myClick():
    #n_t = "Kill Him"+name.get()
    #myLabel = Label(root, text=n_t)
    #myLabel.pack()
#t = Button(root, text="click me", command=myClick, fg="sky blue", bg="black")
#t.pack()
#root.mainloop() 
from tkinter import *
import  math
root = Tk()
root.title("Calculator")
num = Entry(root, width = 45, borderwidth=5)
num.grid(row = 0, column = 0, columnspan=4, padx=10, pady=10)
def button_click(number):
    current = num.get()
    num.delete(0,END)
    num.insert(0,str(current) + str(number))
def clear():
    num.delete(0,END)
    return
def button_add():
    first_number = num.get()
    global f_num
    global mathe
    mathe = "addition"
    f_num =int(first_number)
    num.delete(0,END)
def button_sub():
    first_n = num.get()
    global f_num
    global mathe
    f_num = int(first_n)
    mathe = "subtraction"
    f_num =int(first_n)
    num.delete(0,END)
def button_multi():
    first_n = num.get()
    global f_num
    global mathe
    f_num = int(first_n)
    mathe = "multiplication"
    f_num =int(first_n)
    num.delete(0,END)
def button_div():
    first_n = num.get()
    global f_num
    global mathe
    f_num = int(first_n)
    mathe = "division"
    f_num =int(first_n)
    num.delete(0,END)
def button_equal():
    second_num = num.get()
    num.delete(0,END)
    if mathe == "addition":
        num.insert(0,f_num + int(second_num))
    elif mathe == "subtraction":
        num.insert(0,f_num - int(second_num))
    elif mathe == "multiplication":
        num.insert(0,f_num * int(second_num))
    elif mathe == "division":
        num.insert(0,f_num / int(second_num))



    

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
butt_add = Button(root, text="+", padx=40, pady=20, command= button_add)
butt_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
butt_multi = Button(root, text="*", padx=40, pady=20, command=button_multi)
butt_div = Button(root,text="/",padx=40, pady=20, command=button_div)
but_equal = Button(root, text="=", padx=40, pady=20, command= button_equal)
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)
#button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: button_click())

button_0.grid(row=1,column=0)
button_1.grid(row=1,column=1)
button_2.grid(row=1,column=2)
button_3.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=2,column=3)
button_8.grid(row=3,column=0)
button_9.grid(row=3,column=1)
butt_add.grid(row=3,column=2)
butt_sub.grid(row=3,column=3)
butt_div.grid(row=4,column=0)
butt_multi.grid(row=4,column=1)
but_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=3)
root.mainloop()