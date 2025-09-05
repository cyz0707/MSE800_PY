import sqlite3

def create_connection():
    conn = sqlite3.connect("YBCarRental.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    # create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT PRIMARY KEY,
            password CHAR(50) NOT NULL,
            des TEXT
        )
    ''')

    # create admin table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT PRIMARY KEY,
            password CHAR(50) NOT NULL,
            des TEXT
        )
    ''')

    # create car table 
    # is_available: 0 unavailable, 1 available
    # min_rent_period: default 1 day
    # max_rent_period: default 100 day
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS car (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            is_available INTEGER DEFAULT 1 CHECK (is_available IN (0, 1)),
            min_rent_period INTEGER DEFAULT 1,
            max_rent_period INTEGER DEFAULT 100
        )
    ''')

    ## add a default admin
    # cursor.execute('SELECT * FROM admin WHERE user_name = admin')
    # rows = cursor.fetchall()
    # if len(rows) == 0:
    #     cursor.execute('''
    #         INSERT INTO admin (user_name, password)
    #         VALUES ('admin', '123456');           
    #     ''')

    conn.commit()
    conn.close()