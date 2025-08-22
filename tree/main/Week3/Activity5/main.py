from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import add_student, view_students, delete_student

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Add Student")
    print("6. Show Users and Students")
    print("7. Delete Student by ID")
    print("8. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            name = input("Enter name: ")
            address = input("Enter address: ")
            add_student(name, address)
        elif choice == '6':
            users = view_users()
            students = view_students()
            for user in users:
                print(user)
            for student in students:
                print(student)
        elif choice == '7':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
