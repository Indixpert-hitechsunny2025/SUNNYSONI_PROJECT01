from student_manager import register_new_student, show_all_students

def display_main_menu():
    while True:
        print("\n=== Student Registration System ===")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            register_new_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            print("Exiting the system.Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    display_main_menu()


    