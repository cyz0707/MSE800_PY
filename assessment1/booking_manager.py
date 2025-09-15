from database import create_connection
import sqlite3
from user_manager import print_table_data
from datetime import datetime

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Connection:
    def __init__(self):
        self.conn = create_connection()
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

class Booking:
    def __init__(self, booking_id, user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests):
        self.booking_id = booking_id
        self.user_id = user_id
        self.customer_name = customer_name
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = total_days
        self.daily_rate = daily_rate
        self.total_amount = total_amount
        self.booking_status = booking_status
        self.special_requests = special_requests

    def booking_car(user_id, user_name, car_id, start_date, end_date, special_requests):
        conn = Connection()
        cursor = conn.cursor
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            total_days = (end - start).days
            if total_days <= 0:
                print(bcolors.WARNING + "\nEnd date must be after start date." + bcolors.ENDC)
                return
            
            if start < datetime.now():
                print(bcolors.WARNING + "\nStart date must be in the future." + bcolors.ENDC)
                return
            
            # check car availability
            check_availability_query = '''SELECT COUNT(*) FROM bookings 
                WHERE car_id = ? AND booking_status IN ('pending', 'confirmed') 
                AND (start_date <= ? AND end_date >= ?)'''
            cursor.execute(check_availability_query, (car_id, end, start))
            (count,) = cursor.fetchone()
            if count > 0:
                print(bcolors.WARNING + "\nCar is not available for the selected dates." + bcolors.ENDC)
                return
            
            # get car details
            cursor.execute("SELECT price, min_rent_period, max_rent_period FROM car WHERE car_id = ?", (car_id,))
            car = cursor.fetchone()
            if not car:
                print(bcolors.WARNING + "\nCar not found." + bcolors.ENDC)
                return
            price, min_rent_period, max_rent_period = car
            if total_days < min_rent_period or total_days > max_rent_period:
                print(bcolors.WARNING + f"\nRental period must be between {min_rent_period} and {max_rent_period} days." + bcolors.ENDC)
                return
            total_amount = total_days * price
            print(bcolors.WARNING + f"\nTotal amount for {total_days} days: ${total_amount}" + bcolors.ENDC)

            # insert booking record
            cursor.execute('''
                INSERT INTO bookings (user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, special_requests)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, user_name, car_id, start, end, total_days, price, total_amount, special_requests))
            conn.conn.commit()
            return
        except sqlite3.Error as e:
            print(f"fail: {e}")
        finally:
            conn.conn.close()

    def view_my_booking_datail(user_id):
        conn = Connection()
        cursor = conn.cursor
        try:
            cursor.execute("SELECT customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests FROM bookings WHERE user_id = ?", (user_id,))
            results = cursor.fetchall()
            
            if not results:
                print(bcolors.WARNING + "\nNo Records" + bcolors.ENDC)
                return
            print_table_data(results)
            
        except sqlite3.Error as e:
            print(f"fail: {e}")
        
        finally:
            conn.conn.close()

    def view_all_booking_datail():
        conn = Connection()
        cursor = conn.cursor
        try:
            cursor.execute("SELECT booking_id, user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests FROM bookings")
            results = cursor.fetchall()
            
            if not results:
                print(bcolors.WARNING + "\nNo Records" + bcolors.ENDC)
                return
            print_table_data(results)
            
        except sqlite3.Error as e:
            print(bcolors.FAIL + f"fail: {e}" + bcolors.ENDC)
        
        finally:
            conn.conn.close()

    def manage_booking(booking_id, status):
        conn = Connection()
        cursor = conn.cursor
        try:
            cursor.execute("UPDATE bookings SET booking_status = ? WHERE booking_id = ?", (status, booking_id))
            conn.conn.commit()
            print(bcolors.OKGREEN + f"\nBooking status updated successfully." + bcolors.ENDC)
        except sqlite3.Error as e:
            print(bcolors.FAIL + f"fail: {e}" + bcolors.ENDC)
        finally:
            conn.conn.close()

    def view_pending_booking_datail():
        conn = Connection()
        cursor = conn.cursor
        try:
            cursor.execute("SELECT booking_id, user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests FROM bookings WHERE booking_status = 'pending'")
            results = cursor.fetchall()
            
            if not results:
                print(bcolors.WARNING + "\nNo Records" + bcolors.ENDC)
                return
            print_table_data(results)
            
        except sqlite3.Error as e:
            print(f"fail: {e}")
        
        finally:
            conn.conn.close()

def validate_date_format(date_string):
    # check if the input string is a valid date in the format 'YYYY-MM-DD'
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False