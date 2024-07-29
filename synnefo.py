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

mydb = mysql.connector.connect(
  host="localhost",
  user="sruthy krishnan",
  password="Sruthy@123",
  database="synnefo"
)




cursor = mydb.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        name VARCHAR(100),
        designation VARCHAR(100),
        salary int
    )
''')

while True:
    print('\n1.add\n2.update\n3.delete\n4.search\n5.view all')
    ch = int(input('enter your choice: '))
    if ch == 1:
      
        name = input('enter your name: ')
        designation = input('enter designation: ')
        salary=input("enter the salary:")
        cursor.execute('INSERT INTO employee ( name, designation,salary) VALUES (%s, %s, %s)',
                       (name, designation,salary))
        mydb.commit()
    elif ch == 2:
       
        name = input('enter your new name: ')
        designation= input('enter new designation: ')
        salary=input("enter the salary:")
        cursor.execute('UPDATE employee SET name=%s,WHERE emp_id=%s',
                       (name,designation,salary))
        mydb.commit()
    elif ch == 3:
        id = int(input('enter id of employee to delete: '))
        cursor.execute('DELETE FROM employee WHERE emp_id=%s', (id,))
        mydb.commit()
    elif ch == 4:
        id = int(input('enter id to search: '))
        cursor.execute('SELECT * FROM employee WHERE emp_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}'.format('id', 'name', 'age', 'email', 'position'))
        print('-' * 60)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print('id not available')
    elif ch == 5:
        cursor.execute('SELECT * FROM employee')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}'.format('id', 'name', 'age', 'email', 'position'))
        print('-' * 60)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
    else:
        print('invalid choice.....')