from database import create_connection
import sqlite3
import bcrypt

def hash_password(password):
    """Hash a password with bcrypt"""
    # Convert password to bytes
    password_bytes = password.encode('utf-8')
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def verify_password(password, hashed_password):
    """Verify a password against its hash"""
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)


def add_user(user_name, password):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
        results = cursor.fetchall()
        if results:
            print('\nUsername already exists')
            return
        else:
            hashed_password = hash_password(password)
            cursor.execute("INSERT INTO users (user_name, password) VALUES (?, ?)", (user_name, hashed_password))
            conn.commit()
            print("\nuser added successfully.")
            conn.close()

    except sqlite3.Error as e:
        print(f"\nfail: {e}")
        return False
    
    finally:
        conn.close()

def delete_user_by_id(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?", (id,))
    conn.commit()
    print(f"\nuser deleted successfully.")
    conn.close()

def login_user(user_name, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
    rows = cursor.fetchall()
    if rows:
        stored_hash = rows[0][2]
        if verify_password(password, stored_hash):
            result = {
                "success": True,
                "user_id": rows[0][0], 
                "user_name": rows[0][1]
            }
        else:
            result = {
                "success": False,
                "user_id": None,
                "user_name": None
            }
    conn.close()
    print('login_user 返回:', result)
    return result

def admin_login(user_name, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE user_name = ? AND password = ?", (user_name, password))
    rows = cursor.fetchall()
    return len(rows) > 0

def view_users():
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        if not results:
            print("\nNo Records")
            return
        print_table_data(results)
        
    except sqlite3.Error as e:
        print(f"\nfail: {e}")
    
    finally:
        conn.close()

def view_admin_list():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin")
    rows = cursor.fetchall()
    conn.close()
    return rows

def print_table_data(data):
    # get column names
    columns = list(data[0].keys())
    
    # calculate max width
    col_widths = {}
    for col in columns:
        col_widths[col] = max(len(col), max(len(str(row[col])) for row in data))
    
    # print column name
    header = " | ".join(col.ljust(col_widths[col]) for col in columns)
    print("\n")
    print(header)
    print("-" * len(header))
    
    # print data row
    for row in data:
        data_row = " | ".join(str(row[col]).ljust(col_widths[col]) for col in columns)
        print(data_row)