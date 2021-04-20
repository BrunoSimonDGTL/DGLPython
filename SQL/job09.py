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
SELECT name
FROM job;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()

#job = input("Donne un nom de job:")
job = "IDE"
val = (job,)
print("all the job")
print(mycursor.column_names)
for x in myresult:
    print(x[0])

query = """
SELECT job.name AS job_name, unit.name AS unit_Name, unit.id
FROM job, unit
WHERE job.name = %s AND unit.id = job.unit_fk;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print("all the job")
print(mycursor.column_names)
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
