import mysql.connector

print("connexion")


mydb = mysql.connector.connect(
    host="localhost",
    user="Bruno",
    password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

print(mydb)
""" connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplatforme"
)
request = "SELECT * FROM personne"
curseur = connexion.cursor()
curseur.execute(request)

personnes = curseur.fetchall()

for p in personnes:
    print(p)

connexion.close()
curseur.close() """

# Output :
# (1 : "Pierre", "Laurent", "25")
# (2 : "bob", "bib", "54") \n...
