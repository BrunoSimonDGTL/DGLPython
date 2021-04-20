# Faites un programme qui demande à l’utilisateur d’entrer un ‘group_id’ et
# qui affiche le nom du ‘job’ associé.
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

query = """
SELECT DISTINCT group_id
FROM registration;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" | ")

# group_id = input("\nDonne un group_id:")
group_id = 4620
val = (group_id,)

query = """
SELECT DISTINCT job.name AS job_name
FROM registration, job
WHERE registration.group_id = %s AND registration.job_fk = job.id;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print()
print(mycursor.column_names, "for group_id", val[0])
if not myresult:
    print("Pas de result for student_id:", val[0])
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
