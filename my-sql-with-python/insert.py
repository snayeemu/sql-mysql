import mysql.connector

dbName = 'python_test_db'
myDBConnection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = dbName
)

myCursor = myDBConnection.cursor()

sqlQuery = """
    insert into student(
        roll,
        name
    )
    values(
        '1001',
        'Shaikh Nayeem Uddin'
    )
"""

myCursor.execute(sqlQuery)
myDBConnection.commit()