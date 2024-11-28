import mysql.connector

myDb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password'
)

print(myDb) 