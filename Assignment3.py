import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="COMPWiz11",
                        port="5432")

cur = conn.cursor()

def getAllStudents():
    cur.execute("""SELECT * FROM students;""")
    print(cur.fetchall())
    conn.commit()

def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str):
    cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
(%s,%s,%s,%s);""", (first_name,last_name,email,enrollment_date))
    conn.commit()

def updateStudentEmail(student_id: int, new_email: str): 
    cur.execute("""UPDATE students SET email = %s WHERE student_id = %s;""", (new_email,student_id))
    conn.commit()

def deleteStudent(student_id: str):
    cur.execute("""DELETE FROM students WHERE student_id = %s;""", (student_id))
    conn.commit()

# Being function tests here 
getAllStudents()
print("---------------------------------------------")
addStudent("Quinton", "Tracey", "quinton@gmail.com", "2024-01-01")
getAllStudents()
print("---------------------------------------------")
updateStudentEmail(3, "Jannette.smithers@example.ca")
getAllStudents()
print("---------------------------------------------")
deleteStudent("4")
getAllStudents()



# End function tests here

cur.close()
conn.close()
