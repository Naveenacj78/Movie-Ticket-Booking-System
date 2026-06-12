# utils/menu.py

def main_menu():

    print("\n" + "=" * 50)
    print("      MOVIE TICKET BOOKING SYSTEM")
    print("=" * 50)

    print("1. Admin Login")
    print("2. User Registration")
    print("3. User Login")
    print("4. Exit")

    print("=" * 50)

    return input("Enter Choice: ")


def admin_menu():

    print("\n" + "=" * 50)
    print("           ADMIN DASHBOARD")
    print("=" * 50)

    print("1. Add Movie")
    print("2. Update Movie")
    print("3. Delete Movie")
    print("4. View All Movies")
    print("5. Search Movie")
    print("6. Daily Sales Report")
    print("7. Export Bookings CSV")
    print("8. Export Sales CSV")
    print("9. Logout")

    print("=" * 50)

    return input("Enter Choice: ")


def user_menu():

    print("\n" + "=" * 50)
    print("            USER DASHBOARD")
    print("=" * 50)

    print("1. View Movies")
    print("2. Search Movie")
    print("3. View Available Seats")
    print("4. Book Ticket")
    print("5. Cancel Booking")
    print("6. My Bookings")
    print("7. Generate Receipt")
    print("8. Logout")

    print("=" * 50)

    return input("Enter Choice: ")


def movie_management_menu():

    print("\n" + "=" * 50)
    print("         MOVIE MANAGEMENT")
    print("=" * 50)

    print("1. Add Movie")
    print("2. Update Movie")
    print("3. Delete Movie")
    print("4. View Movies")
    print("5. Back")

    print("=" * 50)

    return input("Enter Choice: ")


def report_menu():

    print("\n" + "=" * 50)
    print("            REPORT MENU")
    print("=" * 50)

    print("1. Daily Sales Report")
    print("2. Export Booking Report")
    print("3. Export Sales Report")
    print("4. Back")

    print("=" * 50)

    return input("Enter Choice: ")


def pause():

    input("\nPress Enter To Continue...")


def clear_screen():

    import os

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")