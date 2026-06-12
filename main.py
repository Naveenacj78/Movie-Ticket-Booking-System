# main.py

from database.database import (
    create_tables,
    create_default_admin
)

from utils.menu import (
    main_menu,
    admin_menu,
    user_menu
)

from services.auth_service import AuthService
from services.booking_service import BookingService
from services.report_service import ReportService
from services.receipt_service import ReceiptService
from services.export_service import ExportService

from models.movie import Movie
from models.seat import Seat


def admin_dashboard():

    while True:

        choice = admin_menu()

        if choice == "1":

            print("\nADD MOVIE")

            title = input("Title: ")
            genre = input("Genre: ")
            show_time = input("Show Time: ")

            try:

                seats = int(
                    input("Total Seats: ")
                )

            except ValueError:

                print("Invalid Seats")
                continue

            movie_id = Movie.add_movie(
                title,
                genre,
                show_time,
                seats
            )

            Seat.create_seats(movie_id)

            print("Movie Added Successfully")

        elif choice == "2":

            try:

                movie_id = int(
                    input("Movie ID: ")
                )

            except ValueError:

                print("Invalid ID")
                continue

            title = input("New Title: ")
            genre = input("New Genre: ")
            show_time = input("New Show Time: ")

            Movie.update_movie(
                movie_id,
                title,
                genre,
                show_time
            )

            print("Movie Updated")

        elif choice == "3":

            try:

                movie_id = int(
                    input("Movie ID: ")
                )

            except ValueError:

                print("Invalid ID")
                continue

            Movie.delete_movie(movie_id)

            print("Movie Deleted")

        elif choice == "4":

            movies = Movie.get_all_movies()

            print("\nMOVIES")

            for movie in movies:

                print(
                    f"\nID: {movie[0]}"
                )

                print(
                    f"Title: {movie[1]}"
                )

                print(
                    f"Genre: {movie[2]}"
                )

                print(
                    f"Show Time: {movie[3]}"
                )

                print(
                    f"Available Seats: {movie[5]}"
                )

        elif choice == "5":

            keyword = input(
                "Movie Name: "
            )

            movies = Movie.search_movie(
                keyword
            )

            for movie in movies:

                print(movie)

        elif choice == "6":

            ReportService.daily_sales_report()

        elif choice == "7":

            ExportService.export_bookings_csv()

        elif choice == "8":

            ExportService.export_sales_csv()

        elif choice == "9":

            print("Logout Successful")
            break

        else:

            print("Invalid Choice")


def user_dashboard(user):

    user_id = user[0]

    while True:

        choice = user_menu()

        if choice == "1":

            movies = Movie.get_all_movies()

            for movie in movies:

                print(
                    f"\nMovie ID: {movie[0]}"
                )

                print(
                    f"Title: {movie[1]}"
                )

                print(
                    f"Genre: {movie[2]}"
                )

                print(
                    f"Show Time: {movie[3]}"
                )

                print(
                    f"Available Seats: {movie[5]}"
                )

        elif choice == "2":

            keyword = input(
                "Movie Name: "
            )

            movies = Movie.search_movie(
                keyword
            )

            for movie in movies:

                print(movie)

        elif choice == "3":

            BookingService.show_available_seats()

        elif choice == "4":

            BookingService.book_ticket(
                user_id
            )

        elif choice == "5":

            BookingService.cancel_booking()

        elif choice == "6":

            BookingService.view_my_bookings(
                user_id
            )

        elif choice == "7":

            ReceiptService.generate_receipt()

        elif choice == "8":

            print("Logout Successful")
            break

        else:

            print("Invalid Choice")


def main():

    create_tables()
    create_default_admin()

    while True:

        choice = main_menu()

        if choice == "1":

            admin = (
                AuthService.login_admin()
            )

            if admin:

                admin_dashboard()

        elif choice == "2":

            AuthService.register_user()

        elif choice == "3":

            user = (
                AuthService.login_user()
            )

            if user:

                user_dashboard(user)

        elif choice == "4":

            print(
                "\nThank You"
            )

            break

        else:

            print(
                "Invalid Choice"
            )


if __name__ == "__main__":
    main()