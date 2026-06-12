# services/auth_service.py

from models.user import User
from models.admin import Admin
from utils.validator import (
    validate_email,
    validate_password
)


class AuthService:

    @staticmethod
    def register_user():

        print("\n===== USER REGISTRATION =====")

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if not validate_email(email):
            print("Invalid Email Format")
            return

        if not validate_password(password):
            print(
                "Password must contain:\n"
                "- 8 characters\n"
                "- Uppercase\n"
                "- Lowercase\n"
                "- Number"
            )
            return

        User.register(
            name,
            email,
            password
        )

    @staticmethod
    def login_user():

        print("\n===== USER LOGIN =====")

        email = input("Email: ")
        password = input("Password: ")

        user = User.login(
            email,
            password
        )

        if user:
            print(
                f"\nWelcome {user[1]}"
            )
            return user

        print("Invalid Credentials")
        return None

    @staticmethod
    def login_admin():

        print("\n===== ADMIN LOGIN =====")

        username = input("Username: ")
        password = input("Password: ")

        admin = Admin.login(
            username,
            password
        )

        if admin:
            print("Admin Login Success")
            return admin

        print("Invalid Admin Credentials")
        return None