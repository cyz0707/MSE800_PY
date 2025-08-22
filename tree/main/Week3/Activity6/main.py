from database import create_table
from manager import add_class, delete_class, view_class

def menu():
    print("\n==== YB College Manager ====")
    print("1. Add Class")
    print("2. Delete Class")
    print("3. View All Classes")
    # print("3. Search User by Name")
    # print("4. Delete User by ID")
    # print("5. Add Student")
    # print("6. Show Users and Students")
    # print("7. Delete Student by ID")
    # print("8. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option: ")
        if choice == '1':
            name = input("Enter class name: ")
            des = input("Enter des name: ")
            add_class(name, des)
        elif choice == '2':
            class_id = int(input("Enter class ID to delete: "))
            delete_class(class_id)
        elif choice == '3':
            classes = view_class()
            for i in classes:
                print(i)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
