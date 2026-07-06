"""
Event Management System
Validation Functions
"""

import re

from common.constants import *


# Name Validation

def validate_name(name):
    """Validate user's name."""

    return len(name.strip()) >= 3


# Email Validation

def validate_email(email):
    """Validate email address."""

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.match(pattern, email))


# Password Validation

def validate_password(password):
    """Validate password."""

    return len(password) >= DEFAULT_PASSWORD_LENGTH


# Phone Number Validation

def validate_phone(phone):
    """Validate phone number."""

    return phone.isdigit() and len(phone) == 10


# Event Capacity Validation

def validate_capacity(capacity):
    """Validate event capacity."""

    return (
        isinstance(capacity, int)
        and MIN_EVENT_CAPACITY <= capacity <= MAX_EVENT_CAPACITY
    )


# Role Validation

def validate_role(role):
    """Validate user role."""

    return role in ROLES


# Event Status Validation

def validate_event_status(status):
    """Validate event status."""

    return status in EVENT_STATUS


# Registration Status Validation

def validate_registration_status(status):
    """Validate registration status."""

    return status in REGISTRATION_STATUS


# Date Validation

def validate_date(date):
    """Validate date format (DD-MM-YYYY)."""

    pattern = r"^\d{2}-\d{2}-\d{4}$"

    return bool(re.match(pattern, date))


# Time Validation

def validate_time(time):
    """Validate time format (HH:MM)."""

    pattern = r"^\d{2}:\d{2}$"

    return bool(re.match(pattern, time))


# ID Validation

def validate_id(user_id):
    """Validate ID."""

    return len(user_id.strip()) > 0


# Menu Choice Validation

def validate_choice(choice, minimum, maximum):
    """Validate menu choice."""

    if not choice.isdigit():

        return False

    choice = int(choice)

    return minimum <= choice <= maximum


# Numeric Validation

def validate_integer(value):
    """Validate integer."""

    try:

        int(value)

        return True

    except ValueError:

        return False


def validate_float(value):
    """Validate float."""

    try:

        float(value)

        return True

    except ValueError:

        return False


# End of File
