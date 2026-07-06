"""
Event Management System
Helper Functions
"""

import os
from datetime import datetime


# Display Functions

def print_line(length=70):
    """Print a separator line."""

    print("=" * length)


def print_heading(title):
    """Print a formatted heading."""

    print_line()
    print(title.center(70))
    print_line()


def print_subheading(title):
    """Print a formatted subheading."""

    print(f"\n{title}")
    print("-" * len(title))


# Date and Time Functions

def current_date():
    """Return current date."""

    return datetime.now().strftime("%d-%m-%Y")


def current_time():
    """Return current time."""

    return datetime.now().strftime("%H:%M:%S")


def current_datetime():
    """Return current date and time."""

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Screen Functions

def clear_screen():
    """Clear terminal screen."""

    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause program execution."""

    input("\nPress Enter to continue...")


# Message Functions

def success(message):
    """Display success message."""

    print(f"\n[SUCCESS] {message}")


def error(message):
    """Display error message."""

    print(f"\n[ERROR] {message}")


def warning(message):
    """Display warning message."""

    print(f"\n[WARNING] {message}")


def info(message):
    """Display information message."""

    print(f"\n[INFO] {message}")


# Input Functions

def get_string(prompt):
    """Read string input."""

    return input(prompt).strip()


def get_integer(prompt):
    """Read integer input."""

    while True:

        try:

            return int(input(prompt))

        except ValueError:

            print("Please enter a valid integer.")


def get_float(prompt):
    """Read float input."""

    while True:

        try:

            return float(input(prompt))

        except ValueError:

            print("Please enter a valid number.")


# Utility Functions

def generate_separator():

    return "=" * 70


def format_title(title):

    return title.upper()


def capitalize_text(text):

    return text.title()


# End of File
