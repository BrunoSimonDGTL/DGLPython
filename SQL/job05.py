import mysql.connector


#prenom = input("donne moi un prenom: ")
#nom =input("Donne moi un nom: ")
prenom = "Amyyy"
nom = "Amy"
print(prenom, nom)

dbName = "runtrack1"
mydb = mysql.connector.connect(
    host="localhost",
    user="Bruno",
    password="",
    database=dbName
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM auteur;")
myresult = mycursor.fetchall()
print("auteur:")
for x in myresult:
    print(x)

mycursor.execute("SELECT * FROM livre;")
myresult = mycursor.fetchall()
print("livre:")
for x in myresult:
    print(x)

# recuperer l'id de l'auteur
query = "SELECT id FROM auteur WHERE prenom = %s AND nom = %s;"
auteur = (prenom, nom)

mycursor.execute(query, auteur)
auteur_id = mycursor.fetchone()
# print(auteur_id)

# recuperer les livres avec le id_auteur
query = "SELECT titre FROM livre WHERE auteur_id = %s;"
mycursor.execute(query, auteur_id)
livre = mycursor.fetchall()

# afficher les titres
print("\nLivre ecrit par", nom, prenom)
for x in livre:
    print(x)

mydb.close()
mycursor.close()
