query='select * from users where username=%s'
      mycursor.execute(query,(username_entry.get()))
      row=mycursor.fetchone()
      if row!=NONE:
        messagebox.showerror('Username Error','Username already taken')
      else: