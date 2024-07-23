import sqlite3
con=sqlite3.connect("new.db")
try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass
# con.execute("insert into student(age,name,mark)values(22,'anu',40)")
# con.commit()

# age=int(input("age"))
# name=str(input("name"))
# mark=float(input("mark"))
# con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
# con.commit()


# a=int(input("enter limit"))
# for i in range(a):
#     age=int(input("age"))
#     name=str(input("name"))
#     mark=float(input("mark"))
#     con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
#     con.commit()


# data=con.execute("select * from student")
# print(data)
# for i in data:
#     print(i)



data=con.execute("select * from student")
print("{:<10}{:<16}{:<10}".format("age","name","mark"))
for i in data:
    # print(i)
    print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[0]))


