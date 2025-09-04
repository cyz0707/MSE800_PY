from database import create_table
from user_manager import add_user, login_user, admin_login, view_users

def menu():
    print("\n==== YB Car Rental ====")
    print('1. Log in')
    print('2. Sign up')
    print('3. Admin login')
    print('4. Show user list')

def main():
    create_table()
    while True:
        menu()
        choice = input('Select an option: ')
        if choice == '1':
            name = input('Enter user name: ')
            password = input('Enter password: ')
            if login_user(name, password):
                print('Log in successfully')
                jump_to_user_interface(name)
                return False
            else:
                print('Wrong user name or password ')
        elif choice == '2':
            user_name = input('Enter user name: ')
            password = input('Enter password: ')
            add_user(user_name, password)
        elif choice == '3':
            classes = admin_login()
            for i in classes:
                print(i)
        elif choice == '4':
            list = view_users()
            for i in list:
                print(i)
        else:
            print('Invalid choice, try again.')

def jump_to_user_interface(name):
    print(f"\n==== Welcome {name} ====")
    print('1. View Cars')
    print('2. View My Detail')

if __name__ == '__main__':
    main()