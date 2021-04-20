# Faites un programme qui demande à l’utilisateur d’entrer un id de ‘student’
# et qui affiche le cumul de point ‘earned’ groupee par ‘skill’
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
FROM student;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" | ")

# student_id = input("\nDonne un student_id:")
student_id = 15
val = (student_id,)

query = """
SELECT skill.name AS skill_name, SUM(job_skill.earned) AS cumul
FROM acquiered_skill, job_skill, skill
WHERE acquiered_skill.student_fk = %s AND acquiered_skill.job_skill_fk = job_skill.id AND job_skill.skill_fk = skill.id
GROUP BY skill.id;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print()
print(mycursor.column_names, "for student", val[0])
if not myresult:
    print("Pas de result for student_id:", val[0])
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
