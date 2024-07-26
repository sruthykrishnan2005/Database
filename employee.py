import sqlite3
con=sqlite3.connect("employee.db")
try:
    con.execute("create table staff(id int primary key,name text,age int,salary real,email id,position text)")
except:
    pass
while True:
    print("1.add")
    print("2.display")
    print("3.update")
    print("4.delete")
    print("5.exit")
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
        data=con.execute("select * from staff")
        print(data)
        for i in data:
            print(i)
    elif ch=='3':
        name_to_update =input("enter name of staff member to update")
        new_salary =float(input("enter new salary"))
        update_query ="update staff set salary =? where name=?"
        con.execute(update_query,(new_salary,name_to_update))
        con.commit()
        print("staff updated successfully")
    elif ch=='4':
        n=input("enter id")
        con.execute("delete from staff where id=?",(n))
        con.commit()
        print("delete successfully")
    elif ch=='5':
        print("exit")
        break



        






