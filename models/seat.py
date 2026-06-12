from database.database import get_connection


class Seat:

    @staticmethod
    def create_seats(movie_id):

        conn = get_connection()
        cursor = conn.cursor()

        rows = ['A', 'B', 'C', 'D', 'E']

        for row in rows:

            for col in range(1, 11):

                seat_number = f"{row}{col}"

                cursor.execute("""
                INSERT INTO Seats(
                movie_id,
                seat_number,
                status
                )
                VALUES(?,?,?)
                """, (
                    movie_id,
                    seat_number,
                    "Available"
                ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_available_seats(movie_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT seat_number
        FROM Seats
        WHERE movie_id=?
        AND status='Available'
        """, (movie_id,))

        seats = cursor.fetchall()

        conn.close()

        return seats

    @staticmethod
    def book_seat(
            movie_id,
            seat_number):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE Seats
        SET status='Booked'
        WHERE movie_id=?
        AND seat_number=?
        """, (
            movie_id,
            seat_number
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def free_seat(
            movie_id,
            seat_number):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE Seats
        SET status='Available'
        WHERE movie_id=?
        AND seat_number=?
        """, (
            movie_id,
            seat_number
        ))

        conn.commit()
        conn.close()