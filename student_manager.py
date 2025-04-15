from storage import load_student_data, save_student_data

def register_new_student():
    print("\n--- Register a New Student ---")
    student = {}
    student['ID'] = input("Enter Student ID: ")
    student['Name'] = input("Enter Name: ")
    student['Contact'] = input("Enter Contact Number: ")
    student['Email'] = input("Enter Email Address: ")
    student['Education'] = input("Enter Education: ")
    student['Year'] = input("Which year did you complete your education? (e.g., 2022): ")

    students = load_student_data()
    students.append(student)
    save_student_data(students)
    print("Student registered successfully!")

def show_all_students():
    print("\n--- All Registered Students ---")
    students = load_student_data()
    if not students:
        print("No students found.")
    for student in students:
        for key, value in student.items():
            print(f"{key}: {value}")
        print("-" * 20)