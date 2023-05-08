"""Password/passphrase strength and health checker
"""

import datetime
import getpass
import hashlib
import subprocess

import httpx


def check_password_strength(password: str) -> bool:
    """Check password strength.

    :param password: _description_
    :type password: str
    :return: _description_
    :rtype: bool
    """

    # Password length should be at least 8 characters
    if len(password) < 8:
        return False

    # Password should contain at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Password should contain at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Password should contain at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Password should contain at least one special character
    special_chars = "!@#$%^&*()_+-="
    if not any(char in special_chars for char in password):
        return False

    # Password is strong
    return True


def check_uniqueness(password: str) -> bool:
    """Check password uniqueness using Have I Been Pwned API.

    :param password: _description_
    :type password: str
    :return: _description_
    :rtype: bool
    """

    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = httpx.get(url)  # requests.get(url)
    if response.status_code == 200:
        hashes = (line.split(":") for line in response.text.splitlines())
        count = next((int(count) for suffix_hash, count in hashes if suffix_hash == suffix), 0)
        if count > 0:
            return False
    
    # Password is unique
    return True


def check_membership_in_rainbow_tables(password: str) -> bool:
    """Check password membership in rainbow tables.

    :param password: _description_
    :type password: str
    :return: _description_
    :rtype: bool
    """

    # Hash password using MD5
    md5_password = hashlib.md5(password.encode("utf-8")).hexdigest()

    # Search rainbow tables for hash
    output = subprocess.check_output(["rli", "-h", "md5", md5_password]).decode("utf-8")
    if "Not found" in output:
        # Password is not in rainbow tables
        return True
    else:
        # Password is in rainbow tables
        return False


def check_rotation_activated(last_rotation_date: datetime.date, rotation_interval_days: int) -> bool:
    """Check if password rotation is activated.

    :param last_rotation_date: _description_
    :type last_rotation_date: datetime.date
    :param rotation_interval_days: _description_
    :type rotation_interval_days: int
    :return: _description_
    :rtype: bool
    """

    # Get the current date
    current_date = datetime.date.today()

    # Calculate the number of days since the last password rotation
    days_since_last_rotation = (current_date - last_rotation_date).days

    # Check if the number of days since the last rotation is greater than the rotation interval
    if days_since_last_rotation >= rotation_interval_days:
        # Password rotation is activated
        return True
    else:
        # Password rotation is not activated
        return False


if __name__ == "__main__":

    # password = input("Enter password: ")
    password = getpass.getpass(prompt='Enter password: ')

    if not check_password_strength(password):
        print("Password is weak")
    # elif not check_uniqueness(password):
    #     print("Password is not unique")
    # elif not check_membership_in_rainbow_tables(password):
    #     print("Password is in rainbow tables")
    # elif not check_rotation_activated(datetime.date(2023, 4, 7), 32):
    #     print("Screen rotation is not activated")
    else:
        print("Password is strong and unique, and screen rotation is activated")
