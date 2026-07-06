"""
==========================================================
Event Management System
Common Decorators
==========================================================
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import time
import logging

from functools import wraps

# ==========================================================
# Execution Time Decorator
# ==========================================================

def execution_time(func):
    """
    Measures the execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"\nExecution Time : {end_time - start_time:.4f} seconds")

        return result

    return wrapper


# ==========================================================
# Exception Handler Decorator
# ==========================================================

def exception_handler(func):
    """
    Handles unexpected exceptions gracefully.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:

            return func(*args, **kwargs)

        except Exception as error:

            print(f"\nError : {error}")

            return None

    return wrapper


# ==========================================================
# Login Required Decorator
# ==========================================================

def login_required(func):
    """
    Allows access only to logged-in users.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):

        if getattr(self, "current_user", None) is None:

            print("\nPlease login first.")

            return None

        return func(self, *args, **kwargs)

    return wrapper


# ==========================================================
# Admin Required Decorator
# ==========================================================

def admin_required(func):
    """
    Allows access only to Admin users.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):

        if getattr(self, "current_user", None) is None:

            print("\nPlease login first.")

            return None

        if self.current_user.role != "Admin":

            print("\nAccess Denied.")

            return None

        return func(self, *args, **kwargs)

    return wrapper


# ==========================================================
# Logger Decorator
# ==========================================================

def logger(func):
    """
    Logs function execution.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        logging.info(f"Executing : {func.__name__}")

        result = func(*args, **kwargs)

        logging.info(f"Completed : {func.__name__}")

        return result

    return wrapper


# ==========================================================
# Confirmation Decorator
# ==========================================================

def confirm_action(func):
    """
    Confirms before performing an action.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        choice = input("\nAre you sure? (Y/N): ").strip().upper()

        if choice == "Y":

            return func(*args, **kwargs)

        print("\nOperation Cancelled.")

        return None

    return wrapper


# ==========================================================
# End of File
# ==========================================================
