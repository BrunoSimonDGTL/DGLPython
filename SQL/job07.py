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

#mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#    print(x)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

query = "SELECT name FROM unit;"
mycursor.execute(query)
myresult = mycursor.fetchall()

print("unit name:")
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
