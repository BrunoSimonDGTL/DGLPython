# Faites un programme qui demande à l’utilisateur d’entrer un id de ‘skill’ et
# qui affiche l’id du ‘student’ ayant le plus de ‘earned’ sur ce skill.
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
SELECT DISTINCT id
FROM skill;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" | ")

# group_id = input("\nDonne un id de skill:")
skill_id = 20
val = (skill_id,)

# SUM(job_skill.earned) AS tot_earned
query = """
SELECT acquiered_skill.student_fk AS student_id
FROM  student, acquiered_skill, job_skill
WHERE job_skill.skill_fk = %s AND 
    job_skill.id = acquiered_skill.job_skill_fk 
GROUP BY acquiered_skill.student_fk
ORDER BY SUM(job_skill.earned) DESC
LIMIT 1;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print()
print(mycursor.column_names, "for skill_id", val[0])
if not myresult:
    print("Pas de result for skill_id:", val[0])
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
