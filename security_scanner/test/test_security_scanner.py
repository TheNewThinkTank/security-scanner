"""unittests for security_scanner.
"""

from security_scanner.src.security_scanner import (  # type: ignore
    check_password_strength,
    # check_membership_in_rainbow_tables
    )

def test_check_password_strength():

    # Test weak password
    password = '1234'
    assert check_password_strength(password) is False

    # Test strong password
    password = 'P@ssw0rd!'
    assert check_password_strength(password) is True


# def test_check_membership_in_rainbow_tables():
#     # Test password that is in the rainbow table
#     password = '123456'
#     assert check_membership_in_rainbow_tables(password) == True

#     # Test password that is not in the rainbow table
#     password = 'P@ssw0rd!'
#     assert check_membership_in_rainbow_tables(password) == False
