from database import create_connection
import sqlite3
from user_manager import print_table_data
from datetime import datetime

def booking_car(user_id, user_name, car_id, start_date, end_date, special_requests):
    conn = create_connection()
    cursor = conn.cursor()
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    total_days = (end - start).days
    if total_days <= 0:
        print("\nEnd date must be after start date.")
        return
    
    if start < datetime.now():
        print("\nStart date must be in the future.")
        return
    
    # check car availability
    check_availability_query = '''SELECT COUNT(*) FROM bookings 
        WHERE car_id = ? AND booking_status IN ('pending', 'confirmed') 
        AND (start_date <= ? AND end_date >= ?)'''
    cursor.execute(check_availability_query, (car_id, end, start))
    (count,) = cursor.fetchone()
    if count > 0:
        print("\nCar is not available for the selected dates.")
        return
    
    # get car details
    cursor.execute("SELECT price, min_rent_period, max_rent_period FROM car WHERE car_id = ?", (car_id,))
    car = cursor.fetchone()
    if not car:
        print("\nCar not found.")
        return
    price, min_rent_period, max_rent_period = car
    if total_days < min_rent_period or total_days > max_rent_period:
        print(f"\nRental period must be between {min_rent_period} and {max_rent_period} days.")
        return
    total_amount = total_days * price
    print(f"\nTotal amount for {total_days} days: ${total_amount}")

    # insert booking record
    cursor.execute('''
        INSERT INTO bookings (user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, special_requests)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, user_name, car_id, start, end, total_days, price, total_amount, special_requests))
    conn.commit()  
    return

def view_my_booking_datail(user_id):
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests FROM bookings WHERE user_id = ?", (user_id,))
        results = cursor.fetchall()
        
        if not results:
            print("\nNo Records")
            return
        print_table_data(results)
        
    except sqlite3.Error as e:
        print(f"fail: {e}")
    
    finally:
        conn.close()

def view_all_booking_datail():
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT booking_id, user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests FROM bookings")
        results = cursor.fetchall()
        
        if not results:
            print("\nNo Records")
            return
        print_table_data(results)
        
    except sqlite3.Error as e:
        print(f"fail: {e}")
    
    finally:
        conn.close()

def manage_booking(booking_id, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE bookings SET booking_status = ? WHERE booking_id = ?", (status, booking_id))
    conn.commit()
    print(f"\nBooking status updated successfully.")
    conn.close()

def view_pending_booking_datail():
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT booking_id, user_id, customer_name, car_id, start_date, end_date, total_days, daily_rate, total_amount, booking_status, special_requests FROM bookings WHERE booking_status = 'pending'")
        results = cursor.fetchall()
        
        if not results:
            print("\nNo Records")
            return
        print_table_data(results)
        
    except sqlite3.Error as e:
        print(f"fail: {e}")
    
    finally:
        conn.close()