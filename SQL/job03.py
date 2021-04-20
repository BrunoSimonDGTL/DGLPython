import mysql.connector
# create database runtrack1

print("connexion")
mydb = mysql.connector.connect(
    host="localhost",
    user="Bruno",
    password=""
)
dbName = "runtrack1"
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Runtrack1;")

mycursor.execute("SHOW DATABASES")

if ((dbName,) in mycursor):
    print("it'in")
else:
    mycursor.execute("CREATE DATABASE " + dbName + ";")

mydb = mysql.connector.connect(
    host="localhost",
    user="Bruno",
    password="",
    database=dbName)

query = """
CREATE TABLE Auteur (
    Id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Nom varchar(30) NOT NULL,
    Prenom varchar(30) NOT NULL); """
print(query)
mycursor = mydb.cursor()
mycursor.execute(query)
print("Tables created successfully ")

query2 = """
CREATE TABLE Livre(
    Id int,
    Titre varchar(100) NOT NULL,
    Auteur_id int NOT NULL);  """

mycursor = mydb.cursor()
mycursor.execute(query2)
print("Tables created successfully ")

mydb.close()
mycursor.close()
