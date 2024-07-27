import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sruthy krishnan",
  password="Sruthy@123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")