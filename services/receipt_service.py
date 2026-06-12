# services/receipt_service.py

import os

from models.booking import Booking


class ReceiptService:

    @staticmethod
    def generate_receipt():

        booking_id = int(
            input(
                "Booking ID: "
            )
        )

        booking = (
            Booking.get_booking(
                booking_id
            )
        )

        if not booking:

            print(
                "Booking Not Found"
            )

            return

        if not os.path.exists(
                "receipts"):
            os.makedirs(
                "receipts"
            )

        filename = (
            f"receipts/"
            f"receipt_"
            f"{booking_id}.txt"
        )

        with open(
                filename,
                "w") as file:

            file.write(
                "MOVIE TICKET RECEIPT\n"
            )

            file.write(
                "=" * 30
            )

            file.write("\n")

            file.write(
                f"Booking ID: "
                f"{booking[0]}\n"
            )

            file.write(
                f"User ID: "
                f"{booking[1]}\n"
            )

            file.write(
                f"Movie ID: "
                f"{booking[2]}\n"
            )

            file.write(
                f"Seat: "
                f"{booking[3]}\n"
            )

            file.write(
                f"Time: "
                f"{booking[4]}\n"
            )

        print(
            f"Receipt Saved:\n"
            f"{filename}"
        )