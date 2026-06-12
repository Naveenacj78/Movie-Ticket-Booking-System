import re


def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(
        pattern,
        email
    ) is not None


def validate_password(password):

    """
    Password Rules:
    8+ chars
    1 uppercase
    1 lowercase
    1 digit
    """

    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    return True


def validate_integer(value):

    try:
        int(value)
        return True

    except ValueError:
        return False