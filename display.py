# student_management/display.py
from .data import students

def view_students():
    """Displays all student records in a tabular format."""
    if not students:
        print("No students found.")
        return

    print("===== Student Records =====")
    print("{:<5} {:<20} {:<10} {:<5}".format("ID", "Name", "Course", "Marks"))
    print("-" * 45)
    for student in students:
        print("{:<5} {:<20} {:<10} {:<5}".format(student['id'], student['name'], student['course'], student['marks']))

def search_student():
    """Searches for a student by ID or name."""
    if not students:
        print("No students found to search.")
        return

    search_term = input("Enter student ID or name to search: ")
    found_students = []
    try:
        search_id = int(search_term)
        for student in students:
            if student['id'] == search_id:
                found_students.append(student)
    except ValueError:
        for student in students:
            if search_term.lower() in student['name'].lower():
                found_students.append(student)

    if not found_students:
        print("Student not found.")
    else:
        print("===== Search Results =====")
        print("{:<5} {:<20} {:<10} {:<5}".format("ID", "Name", "Course", "Marks"))
        print("-" * 45)
        for student in found_students:
            print("{:<5} {:<20} {:<10} {:<5}".format(student['id'], student['name'], student['course'], student['marks']))
