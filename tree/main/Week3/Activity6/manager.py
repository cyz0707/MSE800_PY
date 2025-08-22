from database import create_connection
import sqlite3

def add_class(class_name, des):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO classes (class_name, des) VALUES (?, ?)", (class_name, des))
    conn.commit()
    print(" Class added successfully.")
    conn.close()

def view_class():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Classes")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_class(class_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM classes WHERE class_id = ?", (class_id,))
    conn.commit()
    conn.close()
    print("🗑️ Class deleted.")

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
