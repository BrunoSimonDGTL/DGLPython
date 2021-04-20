import mysql.connector
# Faites un programme qui demande à l’utilisateur d’entrer un ‘group_id’ et
# qui affiche le nom du ‘job’ associé ainsi que le nom de la ‘unit’ associée.

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
SELECT group_id
FROM registration;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" ")

# group_id = input("\nDonne un nom de group_id:")
group_id = 1
val = (group_id,)

query = """
SELECT job.name AS job_name, unit.name AS unit_name
FROM registration, job, unit
WHERE registration.group_id = %s AND registration.job_fk = job.id  AND job.unit_fk = unit.id;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print("\nNames from group_id:", val[0])
print(mycursor.column_names)
if not myresult:
    print("Pas de group_id:", val[0])
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
