# models/user.py

from database.database import get_connection
from utils.password_manager import PasswordManager


class User:

    @staticmethod
    def register(name, email, password):

        conn = get_connection()
        cursor = conn.cursor()

        hashed_password = PasswordManager.hash_password(password)

        try:

            cursor.execute("""
            INSERT INTO Users(name,email,password)
            VALUES(?,?,?)
            """, (name, email, hashed_password))

            conn.commit()

            print("User Registered Successfully")

        except Exception as e:

            print("Registration Error:", e)

        finally:
            conn.close()

    @staticmethod
    def login(email, password):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT user_id,name,email,password
        FROM Users
        WHERE email=?
        """, (email,))

        user = cursor.fetchone()

        conn.close()

        if user:

            if PasswordManager.verify_password(
                    password,
                    user[3]):

                return user

        return None

    @staticmethod
    def get_user(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM Users
        WHERE user_id=?
        """, (user_id,))

        user = cursor.fetchone()

        conn.close()

        return user