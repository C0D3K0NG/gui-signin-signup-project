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

#eye functions
def hide():
  openeye.config(file='images/closeeye.png')
  pass_entry.config(show='*')
  eyebutton.config(command=show)
def show():
  openeye.config(file='images/openeye.png')
  pass_entry.config(show='')
  eyebutton.config(command=hide)    

#gui part
pyglet.font.add_file('fonts/Aladin-Regular.ttf')
pyglet.font.add_file('fonts/AlegreyaSans-Regular.ttf')
login_window = tk.Tk()
login_window.geometry('990x660+270+80') # mentioning the width and height and then by putting + we are giving the distance of the screen from x and y axis
login_window.resizable(0,0) # turns off any resizing of the window
login_window.title('LOGIN PAGE')
bgimage = Image.open(r"images/bg.jpg")
bgImage=ImageTk.PhotoImage(bgimage) #only the file name should be given
bgLabel=Label(login_window,image=bgImage).place(x=0,y=0) #packing the image at grid
# middle x=620 y=120
#HEADING
heading=Label(login_window,
              text="WELCOME USER!",
              font=('Aladin',28),
              bg='#D9D9D9')
heading.place(x=518,y=127)

#EMAIL ADDRESS
email_label = Label(login_window, 
                    text="EMAIL", 
                    bg='#D9D9D9', 
                    font=('Alegreya', 14))
email_label.place(x=518, y=205)

email_entry = Entry(login_window, 
                    width=27,
                    bd=0, 
                    font=('Alegreya', 12))
email_entry.place(x=522, y=240)

email_entry.insert("end", "    Enter email address")
email_entry.bind('<FocusIn>',on_enter_email)
email_entry.bind('<FocusOut>',on_back_email)

#PASSWORD
password=Label(login_window,
               text="PASSWORD",
               bg='#D9D9D9',
               font=('Alegreya',14))
password.place(x=518,y=270)

pass_entry=Entry(login_window,
                width=27,
                bd=0,
                font=('Alegreya',12))
pass_entry.place(x=522,y=305)

pass_entry.insert("end", "    Enter password")
pass_entry.bind('<FocusIn>',on_enter_pass)
pass_entry.bind('<FocusOut>',on_back_pass)

#eye button
openeye=PhotoImage(file='images/openeye.png')
eyebutton=Button(login_window,
                 image=openeye,
                 bd=0,
                 bg="white",
                 activebackground='white',
                 cursor='hand2',
                 command=hide)
eyebutton.place(x=735,y=305)

#forgot password button
forgot=Button(login_window,
              text="Forgot Password?",
              bd=0,
              bg='#D9D9D9',
              activebackground='#D9D9D9',
              cursor='hand2',
              font=('Alegreya',11),
              pady=-10,
              activeforeground='#A3A3A3')
forgot.place(x=655,y=332)

#lOGIN BUTTON
login=Button(login_window,
             text="Login",
             width=22,
             bd=0,
             fg='#FF4106',
              bg='#80D7DF',
              activebackground='#80D7DF',
              cursor='hand2',
              font=('Aladin',18),
              activeforeground='blue'
             )
login.place(x=522,y=375)
#or label
orpng=PhotoImage(file='images/or label.png')
orlabel=Label(login_window,
              image=orpng,
              bg='#D9D9D9')
orlabel.place(x=514,y=440)
#google login
google=PhotoImage(file='images/google.png')

google_login=Button(login_window,
             image=google,
             bd=0,
              bg='#D9D9D9',
              activebackground='#D9D9D9',
              cursor='hand2')
google_login.place(x=555,y=470)

#facebook login
fb=PhotoImage(file='images/fb.png')

fb_login=Button(login_window,
             image=fb,
             bd=0,
              bg='#D9D9D9',
              activebackground='#D9D9D9',
              cursor='hand2')
fb_login.place(x=630,y=470)

#linkedin login
lin=PhotoImage(file='images/lin.png')

lin_login=Button(login_window,
             image=lin,
             bd=0,
              bg='#D9D9D9',
              activebackground='#D9D9D9',
              cursor='hand2')
lin_login.place(x=705,y=470)

#create account label

create_label=Label(login_window,
                   text="Don't have an account?",
                   bg='#D9D9D9',
                   bd=0,
                   font=('Alegreya',13))
create_label.place(x=510,y=520)

create_button=Button(login_window,
             text="Create new one",
             bd=0,
              bg='#D9D9D9',
              activebackground='#D9D9D9',
              cursor='hand2',
              font=('Alegreya',13,'bold underline'),
              activeforeground='#A3A3A3'
             )
create_button.place(x=668,y=513)

login_window.mainloop()