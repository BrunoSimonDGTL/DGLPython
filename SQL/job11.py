import mysql.connector
# Faites un programme qui demande à l’utilisateur d’entrer un id de ‘student’
# et qui affiche le nom des ‘unit’ auxquelles est associé ce ‘student’.

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
SELECT id
FROM student;
"""
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0], end=" ")

# student_id = input("\nDonne un nom de student_id:")
student_id = 25
val = (student_id,)


query = """
SELECT unit.name AS unit_name
FROM student, unit
WHERE student.current_unit_fk = unit.id AND student.id = %s;
"""
mycursor.execute(query, val)
myresult = mycursor.fetchall()

print("\nUnit names from student id:", val[0])
print(mycursor.column_names)
if not myresult:
    print("Pas de unit pour student", val[0])
for x in myresult:
    print(x)

mydb.close()
mycursor.close()
