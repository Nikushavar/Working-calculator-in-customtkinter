#importing libraries
import customtkinter
from customtkinter import *
from math import *
from tkinter import *

#starting customtkinter
root = customtkinter.CTk()
root.title("Simple calculator, but better")
root.geometry("250x350")
root.config(bg="#000000")
customtkinter.set_appearance_mode("dark")
root.resizable(False, False)
customtkinter.set_default_color_theme("dark-blue")
font1=("Arial", 20 ,"bold")
e_var = StringVar()
e = customtkinter.CTkEntry(root,textvariable=e_var,text_font=font1,width=250,fg_color="#000000",border_color="#000000")
e.place(x="0", y="10")

#defining functions which we'll use
def button_click(number):
    current = e_var.get()
    if current == 'error' or current =='undefined':
        e_var.set(str(number))
    else:
        e_var.set(str(current) + str(number))

def button_clear():
    e_var.set('')

def button_add():
    first_number = e_var.get()
    global f_num 
    global math
    math = "addition"
    f_num = float(first_number)
    e_var.set('')

def button_equal():
    second_number = e_var.get()
    e_var.set('')
    global math
    try: 
        if math == "addition":
            e_var.set(f_num + int(second_number))
        if math == "subtraction":
            e_var.set(f_num - int(second_number))
        if math == "multiplication":
            e_var.set(f_num * int(second_number))
        if math == "division":
            e_var.set(f_num / int(second_number))
        if math == "power":
            e_var.set(pow(float(f_num), float(second_number)))
        if math == "sqrt":
            e_var.set(sqrt(f_num)) #gives sqrt of only first number
    except (NameError, ValueError):
        e_var.set('error')
    except ZeroDivisionError:
        e_var.set('undefined')

def button_subtract():
    first_number = e_var.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = float(first_number)
    e_var.set('')

def button_multiply():
    first_number = e_var.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = float(first_number)
    e_var.set('')

def button_divide():
    first_number = e_var.get()
    global f_num 
    global math
    math = "division"
    f_num = float(first_number)
    e_var.set('')

def button_power():
    first_number = e_var.get()
    global f_num
    global math
    math = "power"
    f_num = float(first_number)
    e_var.set('')

def button_sqrt():
    first_number = e_var.get()
    global f_num
    global math
    math = "sqrt"
    f_num = float(first_number)
    e_var.set('') #shows sqrt of only first number

#displaying buttons
button1 = customtkinter.CTkButton(root, command=button_clear, text="C", text_font=font1, width=50, height=2)
button1.place(x=10, y=60)
button2 = customtkinter.CTkButton(root, command=button_sqrt, text="√", text_font=font1, width=50, height=2)
button2.place(x=70, y=60)
button3 = customtkinter.CTkButton(root, command=button_divide, text="/", text_font=font1, width=50, height=2)
button3.place(x=130, y=60)

button4 = customtkinter.CTkButton(root, command=button_multiply, text="x", text_font=font1, width=50, height=2,)
button4.place(x=190, y=60)

button5 = customtkinter.CTkButton(root, command=lambda: button_click(7), text="7", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button5.place(x=10, y=120)
button6 = customtkinter.CTkButton(root, command=lambda: button_click(8), text="8", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button6.place(x=70, y=120)

button7 = customtkinter.CTkButton(root, command=lambda: button_click(9), text="9", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button7.place(x=130, y=120)
button8 = customtkinter.CTkButton(root, command=button_add, text="+", text_font=font1, width=50, height=2)
button8.place(x=190, y=120)
button9 = customtkinter.CTkButton(root, command=lambda: button_click(4), text="4", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button9.place(x=10, y=180)

button10 = customtkinter.CTkButton(root, command=lambda: button_click(5), text="5", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button10.place(x=70, y=180)
button11 = customtkinter.CTkButton(root, command=lambda: button_click(6), text="6", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button11.place(x=130, y=180)
button12 = customtkinter.CTkButton(root, command=button_subtract, text="-", text_font=font1, width=50, height=2)
button12.place(x=190, y=180)

button13 = customtkinter.CTkButton(root, command=lambda: button_click(0), text="0", text_font=font1, width=50, height=2)
button13.place(x=10, y=240)
button14 = customtkinter.CTkButton(root, command=lambda: button_click(1), text="1", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button14.place(x=70, y=240)
button15 = customtkinter.CTkButton(root, command=lambda: button_click(2), text="2", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button15.place(x=130, y=240)

button16 = customtkinter.CTkButton(root, command=lambda: button_click(3), text="3", text_font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#2e2a27")
button16.place(x=190, y=240)
button17 = customtkinter.CTkButton(root, command=button_power, text="^", text_font=font1, width=50, height=2)
button17.place(x=10, y=300)
button18 = customtkinter.CTkButton(root, command=button_equal, text="=", text_font=font1, width=170, height=2)
button18.place(x=70, y=300)
#looping
root.mainloop()