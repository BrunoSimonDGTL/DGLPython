import mysql.connector

print("connexion")
dbname = "laplateforme"
mydb = mysql.connector.connect(
    host="localhost",
    user="Bruno",
    password="",
    database=dbname,
)
mycursor = mydb.cursor()

query = "SELECT name FROM unit WHERE name LIKE '%pool%';"
mycursor.execute(query)
myresult = mycursor.fetchall()

print("unit name containing pool:")
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
