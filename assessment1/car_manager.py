from database import create_connection
import sqlite3

def view_cars():
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM car")
        results = cursor.fetchall()
        
        if not results:
            print("No Records")
            return
        
        # get column names
        columns = list(results[0].keys())
        
        # calculate max width
        col_widths = {}
        for col in columns:
            col_widths[col] = max(len(col), max(len(str(row[col])) for row in results))
        
        # print column name
        header = " | ".join(col.ljust(col_widths[col]) for col in columns)
        print(header)
        print("-" * len(header))
        
        # print data row
        for row in results:
            data_row = " | ".join(str(row[col]).ljust(col_widths[col]) for col in columns)
            print(data_row)
        
    except sqlite3.Error as e:
        print(f"fail: {e}")
    
    finally:
        conn.close()

def add_car(make, year, mileage, is_available, min_rent_period, max_rent_period):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO car (make, year, mileage, is_available, min_rent_period, max_rent_period) VALUES (?, ?, ?, ?, ?, ?)", (make, year, mileage, is_available, min_rent_period, max_rent_period))
    conn.commit()
    print(f"car added successfully.")
    conn.close()

def update_car(id, make, year, mileage, is_available, min_rent_period, max_rent_period):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE car 
        SET make = ?, year = ?, mileage = ?, is_available = ?, min_rent_period = ?, max_rent_period = ?
        WHERE car_id = ?
    """, (make, year, mileage, is_available, min_rent_period, max_rent_period, id))
    conn.commit()
    print(f"car updated successfully.")
    conn.close()

def delete_car(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM car WHERE car_id = ?", (id,))
    conn.commit()
    print(f"car deleted successfully.")
    conn.close()
