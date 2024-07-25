import sqlite3
con=sqlite3.connect("employee.db")
try:
    con.execute("create table staff(id int primary key,name text,age int,salary real,email id,position text)")
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
        id=int(input("enter id"))
        name=(input("enter name"))
        age=int(input("enter age"))
        position=input("enter position")
        salary=float(input("enter salary"))
        con.execute("insert into staff(id,name,age,salary,position)values(?,?,?,?,?)",(id,name,age,salary,position))
        con.commit()
        print("staff added successfully")
    elif ch=='2':
        id=int(input("enter new id"))
        name=str(input("enter new name"))
        age=int(input("enter new age"))
        position=input("enter new position")
        salary=float(input("enter salary"))
        con.execute("update staff set (id,name,age,salary,position) where (id,name,age,salary,position)")
        con.commit()
        data=con.execute("select * from staff")
        print("updated successfully")
    elif ch=='3':
        id=int(input("delete id"))
        name=str(input("delete name"))


     
    



        






