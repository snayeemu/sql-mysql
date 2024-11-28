import mysql.connector

dbName = 'python_test_db'

myDbConnection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = dbName
)

myCursor = myDbConnection.cursor()

sqlQuery = """
    update student
    set roll = '1002'
    where roll = '1001'
"""

myCursor.execute(sqlQuery)
myDbConnection.commit()