import sqlite3

def create_connection():
    conn = sqlite3.connect("YBcollege.db")
    return conn

def create_table():
    print('here')
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL,
            des TEXT
        )
    ''')

    conn.commit()
    conn.close()