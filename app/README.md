# Security Scanner

A package used to check the health and strength of passwords/passphrases.

# How to use
After installing the package use following import:

```Python
from security_scanner import (check_password_strength, check_uniqueness, check_membership_in_rainbow_tables, check_rotation_activated)
```

Then use following commands:

```Python
password = getpass.getpass(prompt='Enter password: ')

if not check_password_strength(password):
    print("Password is weak")
elif not check_uniqueness(password):
    print("Password is not unique")
elif not check_membership_in_rainbow_tables(password):
    print("Password is in rainbow tables")
elif not check_rotation_activated(datetime.date(YEAR, MONTH, DAY), rotation_interval_days):
    print("Screen rotation is not activated")
else:
    print("Password is strong and unique, and screen rotation is activated")
````
