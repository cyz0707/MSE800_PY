from database import create_table
from user_manager import add_user, login_user, admin_login, view_users, delete_user_by_id
from car_manager import view_cars, add_car, delete_car, update_car, booking_car, view_my_booking_datail, view_all_booking_datail, manage_booking, view_pending_booking_datail
from datetime import datetime, timedelta

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
            user_info = login_user(name, password)
            print('user_info', user_info['user_id'])
            if user_info['user_id'] is not None:
                print('\nLog in successfully')
                jump_to_user_interface(user_info)
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
    print('3. View my booking details')

def jump_to_user_interface(user_info):
    while True:
        customer_menu(user_info['user_name'])
        choice = input('Select an option: ')
        if choice == '1':
            view_cars(1)
        elif choice == '2':
            view_cars(1)
            car_id = int(input('Input car id: '))
            start_date = input('Rental start date[YYYY-MM-DD]: ')
            end_date = input('Rental end date[ YYYY-MM-DD]: ')
            special_requests = input('Any special requests: ')
            booking_car(user_info['user_id'], user_info['user_name'], car_id, start_date, end_date, special_requests)
        elif choice == '3':
            view_my_booking_datail(user_info['user_id'])
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
    print('7. View all bookings')
    print('8. Manage bookings')
    print('9. Return to homepage')

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
            view_all_booking_datail()
        elif choice == '8':
            view_pending_booking_datail()
            booking_id = int(input('Enter booking id to manage: '))
            status = int(input("Enter new status (0: pending, 1: confirmed, 2: cancelled): "))
            status_map = {0: 'pending', 1: 'confirmed', 2: 'cancelled'}
            manage_booking(booking_id, status_map.get(status, 0))
        elif choice == '9':
            main()
            return False
        else:
            print('Invalid choice, try again.')

if __name__ == '__main__':
    create_table()
    main()