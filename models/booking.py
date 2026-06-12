from database.database import get_connection


class Booking:

    @staticmethod
    def create_booking(
            user_id,
            movie_id,
            seat_number):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Bookings(
        user_id,
        movie_id,
        seat_number
        )
        VALUES(?,?,?)
        """, (
            user_id,
            movie_id,
            seat_number
        ))

        booking_id = cursor.lastrowid

        cursor.execute("""
        UPDATE Movies
        SET available_seats =
        available_seats - 1
        WHERE movie_id=?
        """, (movie_id,))

        conn.commit()
        conn.close()

        return booking_id

    @staticmethod
    def cancel_booking(
            booking_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT movie_id,
               seat_number
        FROM Bookings
        WHERE booking_id=?
        """, (booking_id,))

        booking = cursor.fetchone()

        if not booking:

            conn.close()
            return None

        movie_id = booking[0]
        seat_number = booking[1]

        cursor.execute("""
        DELETE FROM Bookings
        WHERE booking_id=?
        """, (booking_id,))

        cursor.execute("""
        UPDATE Movies
        SET available_seats =
        available_seats + 1
        WHERE movie_id=?
        """, (movie_id,))

        conn.commit()
        conn.close()

        return movie_id, seat_number

    @staticmethod
    def get_user_bookings(
            user_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
        b.booking_id,
        m.title,
        b.seat_number,
        b.booking_time

        FROM Bookings b

        JOIN Movies m
        ON b.movie_id =
        m.movie_id

        WHERE b.user_id=?
        """, (user_id,))

        bookings = cursor.fetchall()

        conn.close()

        return bookings