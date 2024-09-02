import tkinter as tk
from tkinter import *  #importing all from tkinter module for making gui 
from PIL import Image,ImageTk # from Pillow module import Image and ImageTk class for importing images
import pyglet #importing pyglet module for importing a custom font 

#function part
def on_enter_email(a):
  if email_entry.get() == "    Enter email address":
    email_entry.delete(0,END)
    return None
def on_back_email(a):
  if email_entry.get() == "":
    email_entry.insert("end", "    Enter email address")
    return None
def on_enter_pass(a):
  if pass_entry.get() == "    Enter password":
    pass_entry.delete(0,END)
    return None
def on_back_pass(a):
  if pass_entry.get() == "":
    pass_entry.insert("end", "    Enter password")
    return None
    

#gui part
pyglet.font.add_file('fonts/Aladin-Regular.ttf')
pyglet.font.add_file('fonts/AlegreyaSans-Regular.ttf')
root = tk.Tk()
root.geometry('990x660+270+80') # mentioning the width and height and then by putting + we are giving the distance of the screen from x and y axis
root.resizable(0,0) # turns off any resizing of the window
root.title('LOGIN PAGE')
bgimage = Image.open(r"C:/Users/rajde/Documents/GitHub/PYTHON LANGUAGE/registrationpage/images/bg.jpg")
bgImage=ImageTk.PhotoImage(bgimage) #only the file name should be given
bgLabel=Label(root,image=bgImage).place(x=0,y=0) #packing the image at grid
# middle x=620 y=120
#HEADING
heading=Label(root,
              text="WELCOME USER!",
              font=('Aladin',28),
              bg='#D9D9D9').place(x=518,y=137)

#EMAIL ADDRESS
email_label = Label(root, 
                    text="EMAIL", 
                    bg='#D9D9D9', 
                    font=('Alegreya', 14)).place(x=518, y=230)

email_entry = Entry(root, 
                    width=30,
                    bd=0, 
                    font=('Alegreya', 11))
email_entry.place(x=522, y=265)

email_entry.insert("end", "    Enter email address")

email_entry.bind('<FocusIn>',on_enter_email)
email_entry.bind('<FocusOut>',on_back_email)

#PASSWORD
password=Label(root,
               text="PASSWORD",
               bg='#D9D9D9',
               font=('Alegreya',14)).place(x=518,y=295)
pass_entry=Entry(root,
                width=30,
                bd=0,
                font=('Alegreya',11))
pass_entry.place(x=522,y=330)

pass_entry.insert("end", "    Enter password")
pass_entry.bind('<FocusIn>',on_enter_pass)
pass_entry.bind('<FocusOut>',on_back_pass)

#eye button



root.mainloop()