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
query = "SELECT * FROM promotion;"
mycursor.execute(query)
# print(mycursor.column_names)
myresult = mycursor.fetchall()

# print("promo:")
# for x in myresult:
#    print(x)

query = "SELECT * FROM student;"
mycursor.execute(query)
# print(mycursor.column_names)

name_promo = 'promotion_fk'
myresult = mycursor.fetchall()
# for x in myresult:
#    print(x)

query = """
SELECT promotion.name AS Promo, COUNT(*) AS nb_student
FROM promotion, student
WHERE student.promotion_fk = promotion.id
GROUP BY promotion.id;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()

print(mycursor.column_names)
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
