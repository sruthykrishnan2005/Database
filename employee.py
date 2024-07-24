import sqlite3
con=sqlite3.connect("employee.db")
try:
    con.execute("create table staff(id,name text,age int,salary real,email id,position text)")
except:
    pass
while True:
    print("1.add")
    print("2.update")
    print("3.delete")
    print("4.display")
    print("5.search")
    ch=input("enter your choice")
    if ch=='1':
        id=
        name=str(input("enter name"))
        age=int(input("enter age"))
        position=input("enter position")
        salary=float(input("enter salary"))
        emailid=
        con.execute("insert into staff(id,name,age,salary,emailid,position)values(?,?,?,?,?,?)",(id,name,age,salary,emailid,position))
        con.commit()
        print("employee added successfully")

        






