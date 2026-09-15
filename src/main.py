from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    enter_marks,
    view_result
)


def display_menu():
    print("\n" + "=" * 45)
    print("   STUDENT MANAGEMENT & ACADEMIC SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Enter Marks")
    print("7. View Student Result")
    print("8. Exit")
    print("=" * 45)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            enter_marks()

        elif choice == "7":
            view_result()

        elif choice == "8":
            print("\nThank you for using the Student Management System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()