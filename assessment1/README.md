# YB Car Rental System

A simple car rental management system built with Python and SQLite for managing users, cars, and bookings.

---

## Features

- **User Management**: Registration and login system
- **Car Management**: Add, view, update, and delete cars
- **Booking System**: Make reservations with date validation
- **Admin Panel**: Manage users, cars, and bookings
- **Database**: SQLite for data storage

---

## Project Structure

```
yb-car-rental/
├── main.py              # Main application entry point
├── database.py          # Database setup and connection
├── user_manager.py      # User authentication and management
├── car_manager.py       # Car management operations
├── booking_manager.py   # Booking system logic
├── YBCarRental.db      # SQLite database (created automatically)
└── README.md           # This file
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher

### Steps

1. **Download the project files**
   ```bash
   # Place all .py files in the same folder
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

   The database will be created automatically on first run.

---

## How to Use

### Starting the Application
```bash
python main.py
```

### Main Menu Options
```
==== YB Car Rental ====
1. Log in
2. Sign up  
3. Admin login
```

### Customer Features
- View available cars
- Book a car for specific dates
- View personal booking history

### Admin Features  
- Manage car inventory (add/edit/delete)
- View all users and bookings
- Approve or cancel bookings

---

## Database Schema

The system creates these tables automatically:

- **users**: User accounts (user_id, user_name, password)
- **admin**: Admin accounts (user_id, user_name, password)  
- **car**: Vehicle inventory (car_id, make, year, mileage, price, availability)
- **bookings**: Reservations (booking_id, user_id, car_id, dates, amounts, status)

---

## Default Admin Account

To access admin features, you can create an admin account by modifying the `database.py` file or use the signup option and manually add to admin table.

---

## Sample Usage

1. **First Time Setup**
   - Run `python main.py`
   - Database is created automatically
   - Sign up as a new user

2. **Making a Booking**
   - Login with your account
   - View available cars
   - Select a car and enter dates (YYYY-MM-DD format)
   - Confirm your booking

3. **Admin Operations**
   - Use admin login
   - Add cars to the system
   - Monitor bookings and user activity

---

That's it! Simple car rental management system ready to use.