# services/report_service.py

from database.database import (
    get_connection
)


class ReportService:

    @staticmethod
    def daily_sales_report():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
        m.title,
        COUNT(b.booking_id)

        FROM Movies m

        LEFT JOIN Bookings b
        ON m.movie_id =
        b.movie_id

        GROUP BY m.title
        """)

        report = cursor.fetchall()

        conn.close()

        print(
            "\n===== SALES REPORT ====="
        )

        for row in report:

            print(
                f"{row[0]} "
                f"-> "
                f"{row[1]} Tickets"
            )

    @staticmethod
    def top_movies():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
        m.title,
        COUNT(b.booking_id)
        AS total

        FROM Movies m

        JOIN Bookings b

        ON m.movie_id =
        b.movie_id

        GROUP BY m.title

        ORDER BY total DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        print(
            "\n===== TOP MOVIES ====="
        )

        for row in rows:

            print(
                row[0],
                "-",
                row[1]
            )