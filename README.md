# 🎬 Movie Ticket Booking System

A complete **Movie Ticket Booking System** developed using **Python, Flask, SQLite, Bootstrap, HTML, CSS, and JavaScript**. This project allows users to browse movies, select seats, book tickets, generate receipts, and enables administrators to manage movies, bookings, reports, and analytics.

---

## 📌 Project Overview

The Movie Ticket Booking System is a web-based application designed to simplify movie ticket reservations. Users can register, log in, view available movies, choose seats, and book tickets online. Administrators can manage movies, monitor bookings, generate reports, and analyze sales data.

This project was developed as a **Final Year Project** for academic purposes.

---

## 🚀 Features

### 👤 User Features

* User Registration
* User Login Authentication
* Secure Password Storage
* Browse Available Movies
* Search Movies by Name
* View Movie Details
* Seat Selection System
* Book Movie Tickets
* View Booking History
* Cancel Bookings
* Generate Booking Receipts
* Print Receipts
* Download Receipt as PDF

### 🔑 Admin Features

* Admin Login
* Add Movies
* Edit Movies
* Delete Movies
* Upload Movie Posters
* View All Movies
* Manage Bookings
* Dashboard Statistics
* Daily Sales Reports
* Revenue Analytics
* Export Bookings to CSV
* Export Sales Reports to CSV

### ⚙️ System Features

* SQLite Database
* Exception Handling
* Logging System
* Responsive Bootstrap UI
* PDF Receipt Generation
* CSV Export Functionality
* Search Functionality
* Session Management

---

## 🛠️ Technologies Used

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python      | Backend Programming       |
| Flask       | Web Framework             |
| SQLite      | Database                  |
| HTML5       | Frontend Structure        |
| CSS3        | Styling                   |
| Bootstrap 5 | Responsive UI             |
| JavaScript  | Client-side Functionality |
| ReportLab   | PDF Generation            |
| CSV Module  | Data Export               |
| Werkzeug    | File Upload Handling      |

---

## 📂 Project Structure

```text
movie_ticket_booking/
│
├── app.py
├── main.py
│
├── database/
│   ├── database.py
│   └── movie_booking.db
│
├── models/
│   ├── admin.py
│   ├── user.py
│   ├── movie.py
│   ├── booking.py
│   └── seat.py
│
├── services/
│   └── export_service.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── posters/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── user_dashboard.html
│   ├── movies.html
│   ├── add_movie.html
│   ├── edit_movie.html
│   ├── select_seat.html
│   ├── bookings.html
│   ├── receipt.html
│   ├── reports.html
│   └── analytics.html
│
├── receipts/
├── exports/
│
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Tables

### Admins

```sql
admin_id
username
password
```

### Users

```sql
user_id
name
email
password
```

### Movies

```sql
movie_id
title
genre
show_time
total_seats
available_seats
poster
```

### Seats

```sql
seat_id
movie_id
seat_number
status
```

### Bookings

```sql
booking_id
user_id
movie_id
seat_number
booking_time
```

---

## ⚡ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/movie-ticket-booking-system.git
```

### 2. Navigate to Project

```bash
cd movie-ticket-booking-system
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Application

```bash
python app.py
```

---

## 🌐 Access Application

Open browser:

```text
http://127.0.0.1:5000
```

---

## 🔐 Default Admin Credentials

```text
Username: admin
Password: admin123
```

---

## 📊 Reports & Analytics

The system provides:

* Total Movies
* Total Users
* Total Bookings
* Revenue Analytics
* Sales Reports
* CSV Export Functionality

---

## 📄 Receipt Generation

Each booking generates:

* Booking ID
* Customer Details
* Movie Information
* Seat Number
* Booking Time
* PDF Download Option
* Printable Receipt

---

## 🛡️ Security Features

* User Authentication
* Session Management
* Password Encryption
* Input Validation
* Exception Handling

---

## 🔮 Future Enhancements

* Online Payment Gateway
* Email Ticket Confirmation
* QR Code Ticket Generation
* Mobile App Integration
* Multi-Theater Support
* Real-Time Seat Updates
* AI-Based Movie Recommendations

---

## 👨‍💻 Author

**Naveena C J**

Final Year Project

Department of Computer Science

---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ If you found this project useful, please give it a star on GitHub!
