from database import create_table
from user_manager import add_user, login_user, admin_login, view_users, delete_user_by_id
from car_manager import view_cars, add_car, delete_car, update_car, booking_car

def menu():
    print("\n==== YB Car Rental ====")
    print('1. Log in')
    print('2. Sign up')
    print('3. Admin login')

def main():
    while True:
        menu()
        choice = input('Select an option: ')
        if choice == '1':
            name = input('Enter user name: ')
            password = input('Enter password: ')
            if login_user(name, password):
                print('\nLog in successfully')
                jump_to_user_interface(name)
                return False
            else:
                print('\nWrong user name or password ')
        elif choice == '2':
            user_name = input('Enter user name: ')
            password = input('Enter password: ')
            add_user(user_name, password)
        elif choice == '3':
            name = input('Enter user name: ')
            password = input('Enter password: ')
            if admin_login(name, password):
                print('\nLog in successfully')
                jump_to_admin_interface(name)
                return False
            else:
                print('Wrong user name or password ')
        else:
            print('Invalid choice, try again.')

def customer_menu(name):
    print(f"\n==== User Page ====")
    print(f"\n==== Welcome {name} ====")
    print('1. View available cars')
    print('2. Book a car')
    print('View My Detail')

def jump_to_user_interface(name):
    while True:
        customer_menu(name)
        choice = input('Select an option: ')
        if choice == '1':
            view_cars(1)
        if choice == '2':
            car_id = int(input('Input car id: '))
            start_date = input('Rental start date: ')
            end_date = input('Rental end date: ')
            booking_car(car_id, start_date, end_date)
        else:
            print('Invalid choice, try again.')

def admin_menu(name):
    print(f"\n==== Admin Page ====")
    print(f"\n==== Welcome {name} ====")
    print('1. View cars')
    print('2. Add a car')
    print('3. Delete a car')
    print('4. Update cars details')
    print('5. View users')
    print('6. Delete users')
    print('7. Return to homepage')

def jump_to_admin_interface(name):
    while True:
        admin_menu(name)
        choice = input('Select an option: ')
        if choice == '1':
            view_cars()
        elif choice == '2':
            make = input('Enter car make: ')
            year = int(input('Enter car year: '))
            mileage = int(input('Enter car mileage: '))
            is_available = int(input('Enter availability (1: Yes, 0: No): '))
            min_rent_period = int(input('Enter minimum rent period (days): '))
            max_rent_period = int(input('Enter maximum rent period (days): '))
            price = int(input('Enter price per day: '))
            add_car(make, year, mileage, is_available, min_rent_period, max_rent_period, price)
        elif choice == '3':
            car_id = int(input('Enter the id of the car you want to delete: '))
            delete_car(car_id)
        elif choice == '4':
            id = int(input('Enter car id: '))
            make = input('Enter car make: ')
            year = int(input('Enter car year: '))
            mileage = int(input('Enter car mileage: '))
            is_available = int(input('Enter availability (1: Yes, 0: No): '))
            min_rent_period = int(input('Enter minimum rent period (days): '))
            max_rent_period = int(input('Enter maximum rent period (days): '))
            price = int(input('Enter price per day: '))
            update_car(id, make, year, mileage, is_available, min_rent_period, max_rent_period, price)
        elif choice == '5':
            view_users()
        elif choice == '6':
            user_id = int(input('Enter the id of the user you want to delete: '))
            delete_user_by_id(user_id)
        elif choice == '7':
            main()
            return False
        else:
            print('Invalid choice, try again.')

if __name__ == '__main__':
    create_table()
    main()