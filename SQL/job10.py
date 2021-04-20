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
SELECT group_id
FROM registration;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" ")

#group_id = input("\nDonne un nom de group_id:")
group_id = 1
val = (group_id,)


query = """
SELECT job.name AS job_name
FROM job, registration
WHERE registration.group_id = %s AND registration.job_fk = job.id;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print("\njob names from group_id:", group_id)
print(mycursor.column_names)
if not myresult:
    print("Pas de job pour group_id", group_id)
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
