from database import create_connection
import sqlite3
from user_manager import print_table_data

def view_cars(is_available=None):
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        if is_available is not None:
            cursor.execute("SELECT car_id, make, year, mileage, min_rent_period, max_rent_period, price FROM car WHERE is_available = ?", (is_available,))
        else:
            cursor.execute("SELECT * FROM car")
        results = cursor.fetchall()
        
        if not results:
            print("\nNo Records")
            return
        print_table_data(results)
        
    except sqlite3.Error as e:
        print(f"fail: {e}")
    
    finally:
        conn.close()

def add_car(make, year, mileage, is_available, min_rent_period, max_rent_period, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO car (make, year, mileage, is_available, min_rent_period, max_rent_period, price) VALUES (?, ?, ?, ?, ?, ?, ?)", (make, year, mileage, is_available, min_rent_period, max_rent_period, price))
    conn.commit()
    print(f"\ncar added successfully.")
    conn.close()

def update_car(id, make, year, mileage, is_available, min_rent_period, max_rent_period, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE car 
        SET make = ?, year = ?, mileage = ?, is_available = ?, min_rent_period = ?, max_rent_period = ?, price = ?
        WHERE car_id = ?
    """, (make, year, mileage, is_available, min_rent_period, max_rent_period, price, id))
    conn.commit()
    print(f"\ncar updated successfully.")
    conn.close()

def delete_car(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM car WHERE car_id = ?", (id,))
    conn.commit()
    print(f"\ncar deleted successfully.")
    conn.close()