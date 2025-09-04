import sqlite3

def create_connection():
    conn = sqlite3.connect("YBCarRental.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT PRIMARY KEY,
            password CHAR(50) NOT NULL,
            des TEXT
        )
    ''')

    # add admin
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT PRIMARY KEY,
            password CHAR(50) NOT NULL,
            des TEXT
        )
    ''')
    # cursor.execute('''
    #     INSERT INTO admin (user_name, password)
    #     VALUES ('admin', '123456');           
    # ''')
    # cursor.execute('''
    #     DELETE FROM admin WHERE user_name = 'admin'
    # ''')

    conn.commit()
    conn.close()