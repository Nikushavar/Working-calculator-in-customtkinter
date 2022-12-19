# Importing libraries
import customtkinter
from tkinter import *
from math import *

# Setting up main color scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Template Options
app_title = "Calculator but better" # Application name
geometry = "250x370" # Enter window geometry 
title_bar_color = "grey10" # Specify the color of top bar
title_color = "white" # Title label color
window_color = None # fg_color of window
resizable = True # Resize window dynamically
round_corner = 20 # adjust corner radius

# Template code (to close, change size of window, etc)

def oldxyset(event):
    global oldx, oldy
    oldx = event.x
    oldy = event.y
    
def move_window(event):
    global x, y
    if fullscreen==False:
        y=event.y_root - oldy
        x=event.x_root - oldx
        root.geometry(f'+{x}+{y}')
    
def close_window():
    root.destroy()
    
def frame_mapped(e):
    root.update_idletasks()
    root.overrideredirect(True)
    root.state('normal')
        
def min_window():
    root.update_idletasks()
    root.overrideredirect(False)
    root.state('iconic')

def max_window():
    if resizable==True:
        global fullscreen
        if fullscreen==False:
            root.update_idletasks()
            root.overrideredirect(False)
            root.wm_state('zoomed')
            root.overrideredirect(True)
            root.state('normal')
            fullscreen=True
        else:
            root.geometry(f'+{x}+{y}')
            fullscreen=False
        
def change_cursor(event):
    if (event.x in range(app.winfo_width()-10, app.winfo_width())
        and event.y in range(app.winfo_height()-10, app.winfo_height())):
        root.config(cursor="size_nw_se")
    else:
        root.config(cursor="")
        
def resize(event):
    if root.cget('cursor')=="size_nw_se":
        if event.x>100 and event.y>100:
            root.geometry(f"{event.x_root-x}x{event.y_root-y}")
        
root = customtkinter.CTk() 
root.overrideredirect(1)
root.config(background='#000001')
root.attributes("-transparentcolor", "#000001")
root.geometry(geometry)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

x = root.winfo_x()
y = root.winfo_y()
fullscreen = False

frame_top = customtkinter.CTkFrame(root, corner_radius=round_corner, 
                                   fg_color=title_bar_color,
                                   background_corner_colors=("#000001","#000001","grey10","grey10"))
frame_top.grid(sticky="nwe", row=0)
frame_top.grid_columnconfigure(0, weight=1)
frame_top.grid_rowconfigure(0, weight=1)
frame_top.bind("<ButtonPress-1>", oldxyset)
frame_top.bind("<B1-Motion>", move_window)

app = customtkinter.CTkFrame(root, corner_radius=round_corner, bg_color="#000001", fg_color=window_color,
                             background_corner_colors=(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"],
                                                       customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"],None,None))
app.grid(sticky="nsew", row=0,pady=(28,0))
app.bind("<Map>",frame_mapped)

if resizable==True:
    app.bind("<Motion>", change_cursor)
    app.bind("<B1-Motion>", resize)
    max_button_color = "yellow"
    hover_color = "#ffda71"
else:
    max_button_color = "grey60"
    hover_color = "grey60"

title_label = customtkinter.CTkLabel(frame_top,  width=1, height=60, 
                                     text=app_title, anchor="n", 
                                     text_color=title_color)
title_label.grid(row=0, sticky="w", padx=20, pady=8)
title_label.bind("<ButtonPress-1>", oldxyset)
title_label.bind("<B1-Motion>", move_window)
    
button_close = customtkinter.CTkButton(frame_top, corner_radius=10, width=10, height=10, text="", hover_color="dark red", fg_color="red",
                                       command=close_window)
button_close.grid(row=0, column=2, sticky="ne", padx=(0,15), pady=10)
button_close.configure(cursor="arrow")

button_max = customtkinter.CTkButton(frame_top, corner_radius=10, width=10, height=10, text="", hover_color=hover_color, fg_color=max_button_color,
                                      command=max_window)
button_max.grid(row=0, column=1, sticky="ne", padx=10, pady=10)
button_max.configure(cursor="arrow")

button_min = customtkinter.CTkButton(frame_top, corner_radius=10, width=10, height=10, text="", hover_color="light green", fg_color="green",
                                       command=min_window)
button_min.grid(row=0, column=0, sticky="ne", pady=10)
button_min.configure(cursor="arrow")
# Now we can place any widgets we want above

# Defining variables which we'll use for calculator
font1=("Arial", 20,"bold")
e_var = StringVar()
e = customtkinter.CTkEntry(app, textvariable=e_var, font=font1, width=230, fg_color="#000000", border_color="#000000")
e.place(x=10, y=10)

# Defining functions which we'll use
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
            e_var.set(f_num * float(second_number))
        if math == "division":
            e_var.set(f_num / int(second_number))
        if math == "power":
            e_var.set(pow(float(f_num), float(second_number)))
        if math == "sqrt":
            e_var.set(sqrt(f_num)) # Gives sqrt of only first number
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
    e_var.set('')

# Displaying buttons
button1 = customtkinter.CTkButton(root, command=button_clear, text="C", 
                                  font=font1, width=50)
button1.place(x=10, y=80)
button2 = customtkinter.CTkButton(root, command=button_sqrt, text="√", 
                                  font=font1, width=50)
button2.place(x=70, y=80)
button3 = customtkinter.CTkButton(root, command=button_divide, text="/", 
                                  font=font1, width=50)
button3.place(x=130, y=80)



button4 = customtkinter.CTkButton(root, command=button_multiply, text="x", 
                                  font=font1, width=50)
button4.place(x=190, y=80)

button5 = customtkinter.CTkButton(root, command=lambda: button_click(7), 
                                  text="7", font=font1, width=50, 
                                  fg_color="#1f1f1f", hover_color="#1f1f1f")
button5.place(x=10, y=140)
button6 = customtkinter.CTkButton(root, command=lambda: button_click(8), 
                                  text="8", font=font1, width=50, 
                                  fg_color="#1f1f1f", hover_color="#1f1f1f")
button6.place(x=70, y=140)



button7 = customtkinter.CTkButton(root, command=lambda: button_click(9),
                                  text="9", font=font1, width=50,
                                  fg_color="#1f1f1f", hover_color="#1f1f1f")
button7.place(x=130, y=140)
button8 = customtkinter.CTkButton(root, command=button_add, text="+", 
                                  font=font1, width=50,)
button8.place(x=190, y=140)
button9 = customtkinter.CTkButton(root, command=lambda: button_click(4), 
                                  text="4", font=font1, width=50,
                                  fg_color="#1f1f1f", hover_color="#1f1f1f")
button9.place(x=10, y=200)



button10 = customtkinter.CTkButton(root, command=lambda: button_click(5), 
                                   text="5", font=font1, width=50, 
                                   fg_color="#1f1f1f", hover_color="#1f1f1f")
button10.place(x=70, y=200)
button11 = customtkinter.CTkButton(root, command=lambda: button_click(6), 
                                   text="6", font=font1, width=50,
                                   fg_color="#1f1f1f", hover_color="#1f1f1f")
button11.place(x=130, y=200)
button12 = customtkinter.CTkButton(root, command=button_subtract, text="-", 
                                   font=font1, width=50)
button12.place(x=190, y=200)



button13 = customtkinter.CTkButton(root, command=lambda: button_click(1), 
                                   text="1", font=font1, width=50,
                                   fg_color="#1f1f1f", hover_color="#1f1f1f")
button13.place(x=10, y=260)
button14 = customtkinter.CTkButton(root, command=lambda: button_click(2), 
                                   text="2", font=font1, width=50, 
                                   fg_color="#1f1f1f", hover_color="#1f1f1f")
button14.place(x=70, y=260)
button15 = customtkinter.CTkButton(root, command=lambda: button_click(3), 
                                   text="3", font=font1, width=50, 
                                   fg_color="#1f1f1f", hover_color="#1f1f1f")
button15.place(x=130, y=260)



button16 = customtkinter.CTkButton(root, command=button_power, text="^",
                                   font=font1, width=50)
button16.place(x=190, y=260)
button17 = customtkinter.CTkButton(root, command=lambda: button_click(0), text="0",
                                   font=font1, width=50)
button17.place(x=10, y=320)
button18 = customtkinter.CTkButton(root, command=button_equal, text="=", 
                                   font=font1, width=170)
button18.place(x=70, y=320)

# looping
root.mainloop()