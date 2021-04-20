import mysql.connector

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

mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE auteur")

mycursor = mydb.cursor()
query = "INSERT INTO auteur (nom, prenom) VALUES (%s, %s);"
auteur = [
    ('Peter', 'Pet'),
    ('Amy', 'Amyyy'),
    ('Hannah', 'Hah'),
    ('Michael', 'kel'),
    ('Bob', 'Bib'), ]
mycursor.executemany(query, auteur)
mydb.commit()

print(mycursor.rowcount, "records inserted.")

mycursor.execute("SELECT * FROM auteur;")
myresult = mycursor.fetchall()
print("auteur:")
for x in myresult:
    print(x)

mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE livre;")
mycursor = mydb.cursor()
query = "INSERT INTO livre (id, titre, auteur_id) VALUES (%s, %s, %s);"
book = [
    (1, 'MySQL', 1),
    (2, 'Beginning XML', 2),
    (3, 'Java How to Program', 2),
    (4, 'Thinking in Java', 3),
    (5, 'The Java Programming Language', 4),
    (6, 'Learning Perl', 4),
    (7, 'Programming Perl', 5), ]

mycursor.executemany(query, book)
mydb.commit()

mycursor.execute("SELECT * FROM livre;")
myresult = mycursor.fetchall()
print("livre:")
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
