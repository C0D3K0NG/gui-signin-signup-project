from tkinter import *
from PIL import ImageTk,Image
import pyglet
from tkinter import messagebox
import mysql.connector
#functions
#clear the entry fields after completion of a new register
def clear():
  email_entry.delete(0,END)
  username_entry.delete(0,END)
  password_entry.delete(0,END)
  confirm_entry.delete(0,END)
#redirect to sign in page
def login():
  signup_window.destroy()
  import signin


#connection to my sql and error handling solutions
def connect_database():
  if email_entry.get()=="" and username_entry.get()=="" and password_entry.get()=="" and confirm_entry.get()=="":
    messagebox.showerror('Error','Fill up all the required boxes')
  elif password_entry.get()!=confirm_entry.get():
    messagebox.showerror('Password mismatch','Password is not matching')
  elif check.get()==0:
    messagebox.showerror('Error','Please accept to our terms and conditions')
  else:
    try:
        connect=mysql.connector.connect(host='localhost',user='root',password='7896')
        mycursor=connect.cursor()
        
        
    except:
      messagebox.showerror('Database error','Connection to database is not established')
      return
    try:
      query = 'create database userdata'
      mycursor.execute(query)
      query='use userdata'
      mycursor.execute(query)
      query='create table users(id int auto_increment primary key not null,email varchar(50) not null,username varchar(20) not null,password varchar(20) not null)'
      mycursor.execute(query)
    except:
      mycursor.execute('use userdata')
    try:
            # Check if username exists
      query = 'SELECT * FROM users WHERE username = %s'
      mycursor.execute(query, (username_entry.get(),))
      row = mycursor.fetchone()

      if row:  # Username already exists
                messagebox.showerror('Username Error', 'Username already taken')
      else:
        query='insert into users(email,username,password) values (%s,%s,%s)'
        mycursor.execute(query,(f'{email_entry.get().lower()}',f'{username_entry.get()}',f'{password_entry.get()}'))     
        messagebox.showinfo('Success',f'{username_entry.get()} is successfully registered')
    except:
      messagebox.showerror('Database error','Registration unsuccessful,please try again!')
    connect.commit()
    connect.close()
    
    clear()
    signup_window.destroy()
    import signin
#gui

#fonts
pyglet.font.add_file('fonts/Aladin-Regular.ttf')
pyglet.font.add_file('fonts/AlegreyaSans-Regular.ttf')

#background
signup_window = Tk()
signup_window.geometry('990x660+270+80') # mentioning the width and height and then by putting + we are giving the distance of the screen from x and y axis
signup_window.resizable(0,0) # turns off any resizing of the window
signup_window.title('SIGNUP PAGE')
bgimage = Image.open(r"images/bg.jpg")
bgImage=ImageTk.PhotoImage(bgimage) #only the file name should be given
bgLabel=Label(signup_window,image=bgImage).place(x=0,y=0)

#frame for sign up components
sign_frame=Frame(signup_window,width=270,height=280,bg='#D9D9D9')
sign_frame.place(x=520,y=200)

#create account 
heading=Label(signup_window,
              text="CREATE ACCOUNT!",
              font=('Aladin',29),
              bg='#D9D9D9')
heading.place(x=508,y=118)

#email
email=Label(sign_frame,
              text="EMAIL",
              font=('Alegreya',13),
              bg='#D9D9D9',
              )
email.grid(row=1,column=0,sticky='w',pady=3)

email_entry = Entry(sign_frame,
                    bg='#E7E7E7', 
                    width=28,
                    bd=0, 
                    font=('Alegreya', 11))
email_entry.grid(row=2,column=0,padx=5 )

#username
username=Label(sign_frame,
              text="USERNAME",
              font=('Alegreya',13),
              bg='#D9D9D9',
              )
username.grid(row=3,column=0,sticky='w',pady=3)

username_entry = Entry(sign_frame,
                       bg='#E7E7E7', 
                    width=28,
                    bd=0, 
                    font=('Alegreya', 11))
username_entry.grid(row=4,column=0,padx=5 )

#password
password=Label(sign_frame,
              text="PASSWORD",
              font=('Alegreya',13),
              bg='#D9D9D9',
              )
password.grid(row=5,column=0,sticky='w',pady=3)

password_entry = Entry(sign_frame, 
                       bg='#E7E7E7',
                    width=28,
                    bd=0, 
                    font=('Alegreya', 11))
password_entry.grid(row=6,column=0,padx=5 )

#confirm password
confirm=Label(sign_frame,
              text="CONFIRM PASSWORD",
              font=('Alegreya',13),
              bg='#D9D9D9',
              )
confirm.grid(row=7,column=0,sticky='w',pady=3)

confirm_entry = Entry(sign_frame,
                      bg='#E7E7E7', 
                    width=28,
                    bd=0, 
                    font=('Alegreya', 11))
confirm_entry.grid(row=8,column=0,padx=5 )

#terms and conditions
check=IntVar()
terms_and_conditions=Checkbutton(sign_frame,
                                 text="I agree to the terms & conditions",
                                 bg='#D9D9D9',
                                 activebackground='#D9D9D9',
                                 cursor='hand2',
                                 bd=0, 
                                 font=('Alegreya', 12),
                                 variable=check)
terms_and_conditions.grid(row=9,column=0,pady=5,sticky=W)

#SIGNUP BUTTON
signup=Button(sign_frame,
             text="Create Account",
             width=25,
             bd=0,
             fg='#FF4106',
              bg='#80D7DF',
              activebackground='#80D7DF',
              cursor='hand2',
              font=('Alegreya',13,'bold'),
              activeforeground='blue',
              command=connect_database
             )
signup.grid(row=10,column=0)

#create account label

login_label=Label(sign_frame,
                   text="Already have an account!",
                   bg='#D9D9D9',
                   bd=0,
                   font=('Alegreya',11))
login_label.grid(row=11,column=0,sticky=W,pady=7,padx=16)

login_button=Button(signup_window,
             text="Login!",
             bd=0,
              bg='#D9D9D9',
              activebackground='#D9D9D9',
              cursor='hand2',
              font=('Alegreya',12,'bold underline'),
              activeforeground='#A3A3A3',
              command=login
             )
login_button.place(x=690,y=526)


signup_window.mainloop()