import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE SOFTWARE")
print("SOFTWARE Data base is created")