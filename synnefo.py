# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="sruthy krishnan",
#   password="Sruthy@123",
#   database="synnefo"
# )

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE employee")
# mycursor.execute("CREATE TABLE employee(name VARCHAR(255),designation VARCHAR(255),salary float)")





import mysql.connector

em = mysql.connector.connect(
    host="localhost",
    user="sruthy krishnan", 
    password="Sruthy@123",  
    database="mydatabase"  
)

cursor = em.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employe (
        emp_id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100),
        position VARCHAR(100),
        salary INT
    )
''')

while True:
    print('\n1.add\n2.update\n3.delete\n4.search\n5.view all\n6.groupby\n7.orderby\n8.like')
    ch = int(input('enter your choice: '))
    if ch == 1:
        l= int (input("Enter limit : "))
        for i in range(l):
            id = int(input('enter employee id: '))
            name = input('enter your name: ')
            age = int(input('enter your age: '))
            email = input('enter your email: ')
            pos = input('enter position: ')
            sal = int(input('enter ur salary:'))
            cursor.execute('INSERT INTO employe (emp_id, name, age, email, position, salary) VALUES (%s, %s, %s, %s, %s, %s)',
                        (id, name, age, email, pos, sal))
            em.commit()
    elif ch == 2:
        id = int(input('enter id of employee: '))
        name = input('enter your new name: ')
        age = int(input('enter your new age: '))
        email = input('enter your new email: ')
        pos = input('enter new position: ')
        sal = int(input('enter ur salary:'))
        cursor.execute('UPDATE employe SET name=%s, age=%s, email=%s, position=%s, salary=%s  WHERE emp_id=%s',
                       (name, age, email, pos, sal,id))
        em.commit()
    elif ch == 3:
        id = int(input('enter id of employe to delete: '))
        cursor.execute('DELETE FROM employe WHERE emp_id=%s', (id,))
        em.commit()
    elif ch == 4:
        id = int(input('enter id to search: '))
        cursor.execute('SELECT * FROM employe WHERE emp_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}'.format('id', 'name', 'age', 'email', 'position','salary'))
        print('-' * 60)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format(i[0], i[1], i[2], i[3], i[4],i[5]))
        else:
            print('id not available')
    elif ch == 5:
        cursor.execute('SELECT * FROM employe')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}'.format('id', 'name', 'age', 'email', 'position','salary'))
        print('-' * 60)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format(i[0], i[1], i[2], i[3], i[4],i[5]))
    elif ch==6:
        cursor.execute("SELECT salary,count(*)FROM employe GROUP BY salary")
        data=cursor.fetchall()
        print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format('id','name','age','email','position','salary'))
        for i in data:
            print(i)
        em.commit()
    elif ch==7:
        cursor.execute("select * from employe order by salary desc")
        data=cursor.fetchall()
        print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format('id','name','age','email','position','salary'))
        for i in data:
            print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif ch==8:
        cursor.execute("select * from employe where name like '%m'")
        data=cursor.fetchall()
        print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format('id','name','age','email','position','salary'))
        for i in data:
            print("{:<10}{:<10}{:<10}{:<20}{:<10}{:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    else:
        print('invalid choice.....')