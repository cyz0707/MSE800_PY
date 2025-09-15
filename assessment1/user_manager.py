from database import create_connection
import sqlite3
import bcrypt

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

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def add_user(user_name, password):
        conn = Connection()
        cursor = conn.cursor

        try:
            cursor.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
            results = cursor.fetchall()
            if results:
                print(bcolors.WARNING + '\nUsername already exists' + bcolors.ENDC)
                return
            else:
                hashed_password = hash_password(password)
                cursor.execute("INSERT INTO users (user_name, password) VALUES (?, ?)", (user_name, hashed_password))
                conn.conn.commit()
                print(bcolors.OKGREEN + "\nuser added successfully." + bcolors.ENDC)

        except sqlite3.Error as e:
            print(f"\nfail: {e}")
            return False
        
        finally:
            conn.conn.close()

    def delete_user_by_id(id):
        conn = Connection()
        cursor = conn.cursor
        cursor.execute("DELETE FROM users WHERE user_id = ?", (id,))
        conn.conn.commit()
        print(bcolors.OKGREEN + f"\nuser deleted successfully." + bcolors.ENDC)
        conn.conn.close()

    def login_user(user_name, password):
        conn = Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
        rows = cursor.fetchall()
        try:
            stored_hash = rows[0][2]
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
            return result
        except IndexError:
            print(bcolors.WARNING + "\nUsername does not exist" + bcolors.ENDC)
            return {
                "success": False,
                "user_id": None,
                "user_name": None
            }
        finally:
            conn.conn.close()

    def admin_login(user_name, password):
        conn = Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM admin WHERE user_name = ? AND password = ?", (user_name, password))
        rows = cursor.fetchall()
        return len(rows) > 0

    def view_users():
        conn = Connection()
        cursor = conn.cursor
        try:
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()
            if not results:
                print(bcolors.WARNING+ "\nNo Records" + bcolors.ENDC)
                return
            print_table_data(results)
            
        except sqlite3.Error as e:
            print(f"\nfail: {e}")
        
        finally:
            conn.conn.close()

    def view_admin_list():
        conn = Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM admin")
        rows = cursor.fetchall()
        conn.conn.close()
        return rows

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

def print_table_data(data):
    if not len(data):
        print(bcolors.WARNING+ "\nNo Records" + bcolors.ENDC)
        return
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