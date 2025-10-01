# student_management/functions.py
from .data import students, MAX_STUDENTS, VALID_COURSES
from .display import view_students

def find_student_by_id(student_id):
    """Helper function to find a student by their ID."""
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def add_student():
    """Adds a new student to the student list."""
    if len(students) >= MAX_STUDENTS:
        print("Error: Maximum student limit reached (8).")
        return

    try:
        student_id = int(input("Enter student ID: "))
        if find_student_by_id(student_id):
            print(f"Error: Student with ID {student_id} already exists.")
            return

        name = input("Enter student name: ")
        course = input(f"Enter student course ({', '.join(VALID_COURSES)}): ").upper()
        if course not in VALID_COURSES:
            print("Error: Invalid course.")
            return

        marks = int(input("Enter student marks: "))
        if not (0 <= marks <= 100):
            print("Error: Marks must be between 0 and 100.")
            return

        new_student = {"id": student_id, "name": name, "course": course, "marks": marks}
        students.append(new_student)
        print("Student added successfully.")
    except ValueError:
        print("Error: Invalid input. ID and marks must be integers.")

def update_student():
    """Modifies a student's course or marks."""
    try:
        student_id = int(input("Enter the ID of the student to update: "))
    except ValueError:
        print("Error: Invalid input. ID must be an integer.")
        return

    student = find_student_by_id(student_id)
    if not student:
        print("Student not found.")
        return

    print("Which detail do you want to update?")
    print("1. Course")
    print("2. Marks")
    choice = input("Enter your choice: ")

    if choice == '1':
        new_course = input(f"Enter new course ({', '.join(VALID_COURSES)}): ").upper()
        if new_course not in VALID_COURSES:
            print("Error: Invalid course.")
            return
        student['course'] = new_course
        print("Course updated successfully.")
    elif choice == '2':
        try:
            new_marks = int(input("Enter new marks: "))
            if not (0 <= new_marks <= 100):
                print("Error: Marks must be between 0 and 100.")
                return
            student['marks'] = new_marks
            print("Marks updated successfully.")
        except ValueError:
            print("Error: Invalid input. Marks must be an integer.")
    else:
        print("Invalid choice.")

def delete_student():
    """Removes a student record by ID."""
    try:
        student_id = int(input("Enter the ID of the student to delete: "))
    except ValueError:
        print("Error: Invalid input. ID must be an integer.")
        return

    student_to_delete = find_student_by_id(student_id)
    if student_to_delete:
        students.remove(student_to_delete)
        print("Student deleted successfully.")
    else:
        print("Student not found.")
