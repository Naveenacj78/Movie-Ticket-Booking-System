import sqlite3
import os

# Database Path
DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "movie_booking.db"
)


def get_connection():
    """
    Create Database Connection
    """
    return sqlite3.connect(DB_PATH)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # Admin Table
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Admins(
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # ==========================
    # Users Table
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # ==========================
    # Movies Table
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Movies(
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        show_time TEXT NOT NULL,
        total_seats INTEGER NOT NULL,
        available_seats INTEGER NOT NULL,
        poster TEXT
    )
    """)

    # ==========================
    # Seats Table
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Seats(
        seat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER NOT NULL,
        seat_number TEXT NOT NULL,
        status TEXT DEFAULT 'Available',

        FOREIGN KEY(movie_id)
        REFERENCES Movies(movie_id)
    )
    """)

    # ==========================
    # Bookings Table
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Bookings(
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        seat_number TEXT NOT NULL,
        booking_time TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id)
        REFERENCES Users(user_id),

        FOREIGN KEY(movie_id)
        REFERENCES Movies(movie_id)
    )
    """)

    conn.commit()
    conn.close()


def create_default_admin():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM Admins
    WHERE username = ?
    """, ("admin",))

    admin = cursor.fetchone()

    if not admin:

        cursor.execute("""
        INSERT INTO Admins(
            username,
            password
        )
        VALUES(
            ?,
            ?
        )
        """, (
            "admin",
            "admin123"
        ))

        conn.commit()

        print(
            "Default Admin Created"
        )

    conn.close()


def reset_database():
    """
    Delete old database
    and create new tables
    """

    if os.path.exists(DB_PATH):

        os.remove(DB_PATH)

        print(
            "Old Database Deleted"
        )

    create_tables()
    create_default_admin()

    print(
        "New Database Created"
    )


if __name__ == "__main__":

    create_tables()
    create_default_admin()

    print(
        "Database Ready"
    )