import sqlite3
import time

def create_connection():
    conn = sqlite3.connect("YBCarRental.db")
    return conn

class UserService:
    def get_user(self, user_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result

class OrderService:
    def get_orders(self, user_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings WHERE user_id = ?", (user_id,))
        results = cursor.fetchall()
        conn.close()
        return results
    
def main():
    user_service = UserService()
    order_service = OrderService()
    
    start_time = time.process_time()
    user = user_service.get_user(1)
    print("User Details:", user)
    
    orders = order_service.get_orders(1)
    print("User Orders:", orders)

    end_time = time.process_time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()