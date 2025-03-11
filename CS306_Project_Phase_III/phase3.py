import mysql.connector
from mysql.connector import Error

# Function to establish a connection to the MySQL database
def create_connection():
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="Tan012345678",
            database="cs306project"
        )
        print("Connection established with the database")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

# Function to create a new student record
def create_student(student_id, name, gpa):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO Students (studentid, sname, sgpa) VALUES (%s, %s, %s)"
        cursor.execute(query, (student_id, name, gpa))
        conn.commit()  # Commit changes to the database
        cursor.close()
        conn.close()
        print("INSERT INTO Students (studentid, sname, sgpa) VALUES (",student_id ,",",name,",",gpa,")")

# Function to create a new project record
def create_assigned_project(project_id, deadline, student_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO Project_Assigned (projectid, pdeadline, studentid) VALUES (%s, %s, %s)"
        cursor.execute(query, (project_id, deadline, student_id))
        conn.commit()  # Commit changes to the database
        cursor.close()
        conn.close()
        print("INSERT INTO Project_Assigned (projectid, pdeadline, studentid) VALUES (",project_id,",",deadline,",",student_id,")")

# Function to read all student records
def read_students():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Students"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        print("SELECT * FROM Students")
        return rows

# Function to read all project records
def read_assigned_projects():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM Project_Assigned"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        print("SELECT * FROM Project_Assigned")
        return rows

# Function to update a student's GPA
def update_student_gpa(student_id, new_gpa):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE Students SET sgpa = %s WHERE studentid = %s"
        cursor.execute(query, (new_gpa, student_id))
        conn.commit()  # Commit changes to the database
        cursor.close()
        conn.close()
        print("UPDATE Students SET sgpa = ",new_gpa," WHERE studentid = ",student_id)

# Function to update a project's deadline
def update_assigned_project_deadline(project_id, new_deadline):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE Project_Assigned SET pdeadline = %s WHERE projectid = %s"
        cursor.execute(query, (new_deadline, project_id))
        conn.commit()  # Commit changes to the database
        cursor.close()
        conn.close()
        print("UPDATE Project_Assigned SET pdeadline = ",new_deadline," WHERE projectid = ",project_id)

# Function to delete a student record
def delete_student(student_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM Students WHERE studentid = %s"
        cursor.execute(query, (student_id,))
        conn.commit()  # Commit changes to the database
        cursor.close()
        conn.close()
        print("DELETE FROM Students WHERE studentid = ",student_id)

# Function to delete a project record
def delete_assigned_project(project_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM Project_Assigned WHERE projectid = %s"
        cursor.execute(query, (project_id,))
        conn.commit()  # Commit changes to the database
        cursor.close()
        conn.close()
        print("DELETE FROM Project_Assigned WHERE projectid = ",project_id)

# Main function to demonstrate CRUD operations
def main():
    # Read the initial table
    print("Students initial:")
    for student in read_students():
        print(student)

    print("Projects initial:")
    for project in read_assigned_projects():
        print(project)

    # Create operations
    create_student(11, "Super_User", 4.0)
    create_assigned_project(101, "2023-05-20", 11)

    # Read operations
    print("Students:")
    for student in read_students():
        print(student)

    print("Projects:")
    for project in read_assigned_projects():
        print(project)

    # Update operations
    update_student_gpa(11, 0.0)
    update_assigned_project_deadline(101, "2023-06-01")

    # Read after update
    print("Students after update:")
    for student in read_students():
        print(student)

    print("Projects after update:")
    for project in read_assigned_projects():
        print(project)

    # Delete operations
    delete_student(11)
    delete_assigned_project(101)

    # Read after delete
    print("Students after delete:")
    for student in read_students():
        print(student)

    print("Projects after delete:")
    for project in read_assigned_projects():
        print(project)
    

if __name__ == "__main__":
    main()
