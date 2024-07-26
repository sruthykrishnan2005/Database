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



# data=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     # print(i)
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[0]))



# name=str(input("name"))
# data=con.execute("select * from student where name=?",(name,))
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# data=con.execute("select * from student where age=11")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# age=int(input("age"))
# data=con.execute("select * from student where age=?",(age))
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# data=con.execute("select * from student where age>=12")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))





# data=con.execute("select * from student where mark<=25")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# data=con.execute("update student set age=23 where age=22")
# con.commit()
# data=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# data=con.execute("delete from student where name='appu'")
# con.commit()
# data=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# name=str(input("name"))
# data=con.execute("delete from student where name='anu'")
# con.commit()
# data=con.execute("select * from student where name=?",(name))
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))




# data=con.execute("select * from student where name like 'a%' ")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# data=con.execute("select * from student where name like '%u' ")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# data=con.execute("select * from student order by name desc")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# data=con.execute("select name,sum(mark)from student group by name")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print(i)
#     # print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))




# age=int(input("age"))
# name=str(input("name"))
# mark=float(input("mark"))
# con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
# con.commit()




