import mysql.connector

myDbConnection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password'
)

dbName = 'python_test_db'

myCursor = myDbConnection.cursor()

sqlQuery = "Create database " + dbName 
myCursor.execute(sqlQuery) 