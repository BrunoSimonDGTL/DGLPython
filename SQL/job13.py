import mysql.connector
# Faites un programme qui demande à l’utilisateur d’entrer un id de ‘job’ et
# qui affiche le nom des ‘skill’ prérequis associés

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
SELECT DISTINCT name
FROM job;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" | ")

# job = input("\nDonne un nom de job:")
job = "MEDITATION"
val = (job,)

query = """
SELECT DISTINCT skill.name AS prerequis
FROM job, skill, job_skill
WHERE job.name = %s AND job_skill.job_fk = job.id  AND job_skill.skill_fk = skill.id;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

#print("\nRequired skill from job:", val[0])
print(mycursor.column_names, "for", val[0])
if not myresult:
    print("Pas de job:", val[0])
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
