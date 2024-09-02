from tkinter import *
def button_command():
  print(tetr.get())
  return None
  
root=Tk()
root.geometry("200x300")
tetr=StringVar()
entry1=Entry(root,textvariable=tetr,width="20").pack()
entry1.insert(0,"Enter")
but=Button(root,text="Button",command=button_command).pack()
root.mainloop()