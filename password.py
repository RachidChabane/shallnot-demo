MINIMUM_LENGTH = 12


def is_acceptable(password: str, username: str) -> bool:
    if len(password) < MINIMUM_LENGTH:
        return False
    return username.lower() not in password.lower()
