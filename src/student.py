from database import create_connection


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    email = input("Enter email: ")
    department = input("Enter department: ")
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students (name, email, department, year)
        VALUES (%s, %s, %s, %s)
    """

    values = (name, email, department, year)

    cursor.execute(query, values)
    connection.commit()

    print("Student added successfully!")

    

    cursor.close()
    connection.close()


def view_students():
    print("\n--- All Students ---")

    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM students"
    cursor.execute(query)

    students = cursor.fetchall()

    print("\nID   Name                 Email                  Department   Year")
    print("-" * 70)

    for student in students:
        print(f"{student[0]:<4} {student[1]:<20} {student[2]:<22} {student[3]:<12} {student[4]}")

    cursor.close()
    connection.close()


def search_student():
    print("\n--- Search Student ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID. Please enter a number.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:
        print("\nStudent Found!")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Email: {student[2]}")
        print(f"Department: {student[3]}")
        print(f"Year: {student[4]}")
    else:
        print("Student not found.")

    cursor.close()
    connection.close()
 

def update_student():
    print("\n--- Update Student ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID. Please enter a number.")
        return
    connection = create_connection()
    cursor = connection.cursor()

    # Check whether student exists
    query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    print(f"\nCurrent Name: {student[1]}")
    print(f"Current Email: {student[2]}")
    print(f"Current Department: {student[3]}")
    print(f"Current Year: {student[4]}")

    email = input("\nEnter new email: ")
    department = input("Enter new department: ")
    year = int(input("Enter new year: "))

    query = """
        UPDATE students
        SET email = %s, department = %s, year = %s
        WHERE student_id = %s
    """

    values = (email, department, year, student_id)

    cursor.execute(query, values)
    connection.commit()

    print("\nStudent updated successfully!")

    cursor.close()
    connection.close()    

def delete_student():
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID. Please enter a number.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    print(f"\nStudent: {student[1]}")
    print(f"Email: {student[2]}")
    print(f"Department: {student[3]}")
    print(f"Year: {student[4]}")

    confirm = input("\nAre you sure you want to delete this student? (yes/no): ")

    if confirm.lower() == "yes":
        query = "DELETE FROM students WHERE student_id = %s"

        cursor.execute(query, (student_id,))
        connection.commit()

        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")

    cursor.close()
    connection.close()    

def enter_marks():
    print("\n--- Enter Marks ---")

    try:
        student_id = int(input("Enter student ID: "))
        subject_id = int(input("Enter subject ID: "))
        marks = int(input("Enter marks (0-100): "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if marks < 0 or marks > 100:
        print("Invalid marks. Marks must be between 0 and 100.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    # Check student
    cursor.execute(
        "SELECT * FROM students WHERE student_id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    # Check subject
    cursor.execute(
        "SELECT * FROM subjects WHERE subject_id = %s",
        (subject_id,)
    )

    subject = cursor.fetchone()

    if not subject:
        print("Subject not found.")
        cursor.close()
        connection.close()
        return

    # Check if marks already exist
    query = """
        SELECT * FROM marks
        WHERE student_id = %s AND subject_id = %s
    """

    cursor.execute(query, (student_id, subject_id))

    existing_marks = cursor.fetchone()

    if existing_marks:
        print("Marks already entered for this student and subject.")
        cursor.close()
        connection.close()
        return

    # Insert marks
    query = """
        INSERT INTO marks (student_id, subject_id, marks)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (student_id, subject_id, marks))
    connection.commit()

    print("Marks added successfully!")

    cursor.close()
    connection.close()

def view_result():
    print("\n--- Student Result ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID. Please enter a number.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    # Get student details
    query = """
        SELECT name, department, year
        FROM students
        WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    print(f"\nStudent: {student[0]}")
    print(f"Department: {student[1]}")
    print(f"Year: {student[2]}")

    # Get marks
    query = """
        SELECT sub.subject_name, m.marks
        FROM marks m
        JOIN subjects sub
            ON m.subject_id = sub.subject_id
        WHERE m.student_id = %s
    """

    cursor.execute(query, (student_id,))
    marks = cursor.fetchall()

    if not marks:
        print("\nNo marks found for this student.")
        cursor.close()
        connection.close()
        return

    print("\nSubject                         Marks")
    print("-" * 40)

    total = 0

    for subject, mark in marks:
        print(f"{subject:<30} {mark}")
        total += mark

    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    result = "PASS" if average >= 50 else "FAIL"

    print("-" * 40)
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")

    cursor.close()
    connection.close()