from database import create_table
from user_manager import User
from car_manager import Car
from booking_manager import Booking, validate_date_format

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# colored print messages
WARNING_MSG = bcolors.WARNING + "\nInvalid input. Please try again."  + bcolors.ENDC
SUCCESS_MSG = bcolors.OKGREEN + "\nLog in successfully."  + bcolors.ENDC
WRONG_MSG = bcolors.FAIL + "\nWrong user name or password."  + bcolors.ENDC
FORMAT_MSG = bcolors.WARNING + "\nInvalid date format. Please use YYYY-MM-DD."  + bcolors.ENDC

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
            try:
                name = input('Enter user name: ')
                password = input('Enter password: ')
                user_info = User.login_user(name, password)
                print('user_info', user_info['user_id'])
                if user_info['user_id'] is not None:
                    print(SUCCESS_MSG)
                    jump_to_user_interface(user_info)
                    return False
                else:
                    print(WRONG_MSG)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '2':
            try:
                user_name = input('Enter user name: ')
                password = input('Enter password: ')
                User.add_user(user_name, password)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '3':
            try:
                name = input('Enter user name: ')
                password = input('Enter password: ')
                if User.admin_login(name, password):
                    print(SUCCESS_MSG)
                    jump_to_admin_interface(name)
                    return False
                else:
                    print(WRONG_MSG)
            except ValueError:
                print(WARNING_MSG)
        else:
            print(WARNING_MSG)

def customer_menu(name):
    print(f"\n==== User Page ====")
    print(f"\n==== Welcome {name} ====")
    print('1. View available cars')
    print('2. Book a car')
    print('3. View my booking details')
    print('4. Return to homepage')

def jump_to_user_interface(user_info):
    while True:
        customer_menu(user_info['user_name'])
        choice = input('Select an option: ')
        if choice == '1':
            Car.view_cars(1)
        elif choice == '2':
            try:
                Car.view_cars(1)
                car_id = int(input('Input car id: '))
                start_date = input('Rental start date[YYYY-MM-DD]: ')
                while validate_date_format(start_date) is False:
                    print(FORMAT_MSG)
                    start_date = input('Rental start date[YYYY-MM-DD]: ')
                end_date = input('Rental end date[ YYYY-MM-DD]: ')
                while validate_date_format(end_date) is False:
                    print(FORMAT_MSG)
                    end_date = input('Rental end date[ YYYY-MM-DD]: ')
                special_requests = input('Any special requests: ')
                Booking.booking_car(user_info['user_id'], user_info['user_name'], car_id, start_date, end_date, special_requests)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '3':
            Booking.view_my_booking_datail(user_info['user_id'])
        elif choice == '4':
            main()
            return False
        else:
            print(WARNING_MSG)

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
            Car.view_cars()
        elif choice == '2':
            try:
                make = input('Enter car make: ')
                year = int(input('Enter car year: '))
                mileage = int(input('Enter car mileage: '))
                is_available = int(input('Enter availability (1: Yes, 0: No): '))
                min_rent_period = int(input('Enter minimum rent period (days): '))
                max_rent_period = int(input('Enter maximum rent period (days): '))
                price = int(input('Enter price per day: '))
                Car.add_car(make, year, mileage, is_available, min_rent_period, max_rent_period, price)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '3':
            try:
                car_id = int(input('Enter the id of the car you want to delete: '))
                Car.delete_car(car_id)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '4':
            try:
                id = int(input('Enter car id: '))
                make = input('Enter car make: ')
                year = int(input('Enter car year: '))
                mileage = int(input('Enter car mileage: '))
                is_available = int(input('Enter availability (1: Yes, 0: No): '))
                min_rent_period = int(input('Enter minimum rent period (days): '))
                max_rent_period = int(input('Enter maximum rent period (days): '))
                price = int(input('Enter price per day: '))
                Car.update_car(id, make, year, mileage, is_available, min_rent_period, max_rent_period, price)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '5':
            User.view_users()
        elif choice == '6':
            try:
                user_id = int(input('Enter the id of the user you want to delete: '))
                User.delete_user_by_id(user_id)
            except ValueError:
                print(WARNING_MSG)
        elif choice == '7':
            Booking.view_all_booking_datail()
        elif choice == '8':
            try:
                Booking.view_all_booking_datail()
                booking_id = int(input('Enter booking id to manage: '))
                status = int(input("Enter new status (0: pending, 1: confirmed, 2: cancelled, 3: completed): "))
                status_map = {0: 'pending', 1: 'confirmed', 2: 'cancelled', 3: 'completed'}
                Booking.manage_booking(booking_id, status_map.get(status, 0))
            except ValueError:
                print(WARNING_MSG)
        elif choice == '9':
            main()
            return False
        else:
            print(WARNING_MSG)

if __name__ == '__main__':
    create_table()
    main()