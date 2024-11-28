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
    Create table Student(
        roll varchar(4),
        name varchar(40)
    )
"""



myCursor.execute(sqlQuery)
