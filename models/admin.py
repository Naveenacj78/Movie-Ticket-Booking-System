# models/admin.py

from database.database import get_connection


class Admin:

    @staticmethod
    def login(username, password):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Admins
        WHERE username=? AND password=?
        """, (username, password))

        admin = cursor.fetchone()

        conn.close()

        return admin