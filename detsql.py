import sqlite3
con=sqlite3.connect("new.db")
try:
    con.execute("create table details(name text,place text,cont_no int,address text)")
except:
    pass
# name=str(input("name"))
# place=str(input("place"))
# cont_no=int(input("cont_no"))
# address=str(input("address"))
# con.execute("insert into details(name,place,cont_no,address)values(?,?,?,?)",(name,place,cont_no,address))
# con.commit()


# data=con.execute("select student.name,student.age,student.mark,details.place,details.cont_no,details.address from student inner join details on student.name=details.name")
# for i in data:
#     print(i)



# data=con.execute("select student.name,student.age,student.mark,details.place,details.cont_no,details.address from student left join details on student.name=details.name")
# for i in data:
#     print(i)



# data=con.execute("select student.name,student.age,student.mark,details.place,details.cont_no,details.address from details left join student on student.name=details.name")
# for i in data:
#     print(i)





# data=con.execute("select student.name,student.age,student.mark,details.place,details.cont_no,details.address from student cross join details")
# for i in data:
#     print(i)