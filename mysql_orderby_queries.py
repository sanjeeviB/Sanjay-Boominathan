import mysql.connector

#import MySQLdb

mydb = mysql.connector.connect(
  host="localhost",
  user="sanjeevi",
  password="1234",
  database="testdb"
)
mycursor= mydb.cursor()
mycursor.execute(("SELECT VERSION()"))
data = mycursor.fetchone()
print ("Database version : %s " % data)
#sql = "SELECT * FROM students ORDER BY name"
sql = "SELECT * FROM students ORDER BY age DESC"

mycursor.execute(sql)
myresult= mycursor.fetchall()
for result in myresult:
    print(result)

mydb.commit()
mydb.close()