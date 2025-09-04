from database import create_connection
import sqlite3

def add_user(user_name, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * from users WHERE user_name = ?', (user_name,))
    rows = cursor.fetchall()
    if len(rows):
        print('--------')
        print('User already exists')
        print('--------')
        return
    cursor.execute("INSERT INTO users (user_name, password) VALUES (?, ?)", (user_name, password))
    conn.commit()
    print(" user added successfully.")
    conn.close()

def login_user(user_name, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * from users WHERE user_name = ? AND password = ?', (user_name, password))
    rows = cursor.fetchall()
    return len(rows) > 0

def admin_login(user_name, password):
    return

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_admin_list():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin")
    rows = cursor.fetchall()
    conn.close()
    return rows