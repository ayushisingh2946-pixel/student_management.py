students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"Name": name, "Roll": roll})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\nStudent Records:")
    for student in students:
        print(f"Name: {student['Name']}, Roll No: {student['Roll']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["Roll"] == roll:
            print(f"Found: Name = {student['Name']}, Roll = {student['Roll']}\n")
            return

    print("Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.\n")