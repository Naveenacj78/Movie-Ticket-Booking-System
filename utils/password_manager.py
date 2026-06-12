# utils/password_manager.py

import bcrypt


class PasswordManager:

    @staticmethod
    def hash_password(password):
        """
        Convert plain password into hashed password
        """

        password_bytes = password.encode('utf-8')

        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(
            password_bytes,
            salt
        )

        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(
            plain_password,
            hashed_password):
        """
        Verify login password
        """

        plain_password = plain_password.encode('utf-8')

        hashed_password = hashed_password.encode('utf-8')

        return bcrypt.checkpw(
            plain_password,
            hashed_password
        )


# Testing Module
if __name__ == "__main__":

    password = "Admin@123"

    print("\nOriginal Password:")
    print(password)

    hashed = PasswordManager.hash_password(password)

    print("\nHashed Password:")
    print(hashed)

    print("\nVerification:")

    if PasswordManager.verify_password(
            "Admin@123",
            hashed):
        print("Password Matched")

    else:
        print("Invalid Password")