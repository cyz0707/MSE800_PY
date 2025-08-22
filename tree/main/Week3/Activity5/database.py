import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            Stu_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Stu_name TEXT NOT NULL,
            Stu_address TEXT NOT NULL UNIQUE
        )
    ''')
        
    conn.commit()
    conn.close()

 # def create_table():
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             address TEXT NOT NULL,
#             class_id INTEGER NOT NULL
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Class (
#             class_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             class_name TEXT NOT NULL
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Subjects (
#             subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             subject_name TEXT NOT NULL,
#             class_id INTEGER NOT NULL
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Lecturer (
#             lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             lecturer_name TEXT NOT NULL,
#             class_id INTEGER NOT NULL,
#             subject_id INTEGER NOT NULL
#         )
#     ''')
