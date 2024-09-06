import mysql.connector

connect=mysql.connector.connect(host='localhost',user='root',password='7896',database='userdata')
mycursor=connect.cursor()
username=str(input("Enter the username to search the password for: "))
query="select password from users where username=%s"
mycursor.execute(query,(username,))
myresult = mycursor.fetchone()
password=str(input("Enter the password: "))
for x in myresult:
  if x==password:
    print("success")
  else:
    print("failed")
  

