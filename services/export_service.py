import csv
import os

from database.database import (
    get_connection
)


class ExportService:

    @staticmethod
    def export_bookings_csv():

        os.makedirs(
            "exports",
            exist_ok=True
        )

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM Bookings
        """)

        rows = cursor.fetchall()

        with open(
            "exports/bookings.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Booking ID",
                "User ID",
                "Movie ID",
                "Seat Number",
                "Booking Time"
            ])

            writer.writerows(rows)

        conn.close()

    @staticmethod
    def export_sales_csv():

        os.makedirs(
            "exports",
            exist_ok=True
        )

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

        rows = cursor.fetchall()

        with open(
            "exports/sales_report.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Movie Name",
                "Tickets Sold"
            ])

            writer.writerows(rows)

        conn.close()