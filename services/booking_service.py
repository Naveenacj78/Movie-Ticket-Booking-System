# services/booking_service.py

from models.booking import Booking
from models.seat import Seat
from models.movie import Movie
from utils.logger import log_info


class BookingService:

    @staticmethod
    def show_available_seats():

        movie_id = int(
            input("Movie ID: ")
        )

        seats = Seat.available_seats(
            movie_id
        )

        print("\nAvailable Seats\n")

        for seat in seats:
            print(seat[0], end=" ")

        print()

    @staticmethod
    def book_ticket(user_id):

        movie_id = int(
            input("Movie ID: ")
        )

        seat_number = input(
            "Seat Number: "
        ).upper()

        seats = Seat.available_seats(
            movie_id
        )

        available = [
            seat[0]
            for seat in seats
        ]

        if seat_number not in available:
            print(
                "Seat Not Available"
            )
            return

        booking_id = Booking.create_booking(
            user_id,
            movie_id,
            seat_number
        )

        Seat.book_seat(
            movie_id,
            seat_number
        )

        log_info(
            f"Booking {booking_id} "
            f"Created"
        )

        print(
            f"Booking Success\n"
            f"Booking ID: {booking_id}"
        )

    @staticmethod
    def cancel_booking():

        booking_id = int(
            input("Booking ID: ")
        )

        result = Booking.cancel_booking(
            booking_id
        )

        if result:

            movie_id = result[0]
            seat_number = result[1]

            Seat.free_seat(
                movie_id,
                seat_number
            )

            print(
                "Booking Cancelled"
            )

        else:

            print(
                "Booking Not Found"
            )

    @staticmethod
    def view_my_bookings(
            user_id):

        bookings = (
            Booking.get_user_bookings(
                user_id
            )
        )

        print(
            "\n===== BOOKINGS ====="
        )

        for booking in bookings:

            print(
                f"\nBooking ID: "
                f"{booking[0]}"
            )

            print(
                f"Movie: "
                f"{booking[1]}"
            )

            print(
                f"Seat: "
                f"{booking[2]}"
            )

            print(
                f"Date: "
                f"{booking[3]}"
            )