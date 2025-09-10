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
            password CHAR(50) NOT NULL
        )
    ''')

    # create admin table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT PRIMARY KEY,
            password CHAR(50) NOT NULL
        )
    ''')

    # create car table 
    # is_available: 0 unavailable, 1 available
    # min_rent_period: default 1 day
    # max_rent_period: default 100 days
    # price: default 100 / per day
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS car (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            is_available INTEGER DEFAULT 1 CHECK (is_available IN (0, 1)),
            min_rent_period INTEGER DEFAULT 1,
            max_rent_period INTEGER DEFAULT 100,
            price INTEGER DEFAULT 100
        )
    ''')

    # # create customers table
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS customers (
    #         customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         first_name TEXT NOT NULL,
    #         last_name TEXT NOT NULL,
    #         email TEXT UNIQUE NOT NULL,
    #         phone TEXT NOT NULL,
    #         license_number TEXT UNIQUE NOT NULL,
    #         date_of_birth DATE NOT NULL,
    #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #     )
    # ''')
    
    # create bookings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            customer_name TEXT NOT NULL,
            car_id INTEGER NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            total_days INTEGER NOT NULL,
            daily_rate REAL NOT NULL,
            total_amount REAL NOT NULL,
            booking_status TEXT DEFAULT 'pending' CHECK (
                booking_status IN ('pending', 'confirmed', 'cancelled', 'completed')
            ),
            special_requests TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES customers (user_id),
            FOREIGN KEY (car_id) REFERENCES cars (car_id)
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