"""
Event Management System
Account Services
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import hashlib

# ==========================================================
# Local Project Imports
# ==========================================================

from accounts.models import *

from common.constants import *
from common.helpers import *
from common.validators import *
from common.permissions import *
from common.decorators import *
from common.exceptions import *


class AccountService:

    def __init__(self, database):

        self.database = database

        self.current_user = None


    # Hash Password

    @staticmethod
    def hash_password(password):

        return hashlib.sha256(

            password.encode()

        ).hexdigest()


    # Verify Password

    @staticmethod
    def verify_password(password, hashed_password):

        return (

            hashlib.sha256(

                password.encode()

            ).hexdigest()

            == hashed_password

        )


    # Register User

    @exception_handler
    def register_user(self):

        print_heading("User Registration")

        name = input("Enter Name           : ")

        if not validate_name(name):
            raise ValidationError("Invalid Name")

        email = input("Enter Email          : ")

        if not validate_email(email):
            raise ValidationError("Invalid Email")

        password = input("Enter Password       : ")

        if not validate_password(password):
            raise ValidationError("Invalid Password")

        role = input(
            "Role (Admin/Student/Faculty/Coordinator/Registrar) : "
        )

        if not validate_role(role):
            raise ValidationError("Invalid Role")

        phone = input("Enter Phone Number   : ")

        if not validate_phone(phone):
            raise ValidationError("Invalid Phone Number")

        password = self.hash_password(password)

        query = """
        INSERT INTO users
        (
            name,
            email,
            password,
            role,
            phone,
            status,
            created_at
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?
        )
        """

        values = (

            None,

            name,

            email,

            password,

            role,

            phone,

            "Active",

            current_datetime()

        )

        self.database.execute(

            query,

            values

        )

        print("\nUser Registered Successfully.")


    # Login User

    @exception_handler
    def login(self):

        print_heading("User Login")

        email = input("Email    : ")

        password = input("Password : ")

        password = self.hash_password(password)

        query = """
        SELECT *
        FROM users
        WHERE email = ?
        AND password = ?
        """

        self.database.execute(

            query,

            (
                email,
                password
            )

        )

        user = self.database.fetch_one()

        if user is None:

            raise AuthenticationError(
                "Invalid Email or Password"
            )

        self.current_user = user

        print("\nLogin Successful.")

        return True


    # Logout

    @login_required
    def logout(self):

        print(f"\nGood Bye {self.current_user[1]}")

        self.current_user = None

        print("Logout Successful.")
        # View Profile

    @login_required
    def view_profile(self):

        print_heading("User Profile")

        print(f"ID         : {self.current_user[0]}")
        print(f"Name       : {self.current_user[1]}")
        print(f"Email      : {self.current_user[2]}")
        print(f"Role       : {self.current_user[4]}")
        print(f"Phone      : {self.current_user[5]}")
        print(f"Status     : {self.current_user[6]}")
        print(f"Created At : {self.current_user[7]}")


    # Update Phone Number

    @login_required
    @exception_handler
    def update_phone(self):

        phone = input("Enter New Phone Number : ")

        if not validate_phone(phone):

            raise ValidationError("Invalid Phone Number")

        query = """
        UPDATE users
        SET phone = ?
        WHERE id = ?
        """

        self.database.execute(

            query,

            (
                phone,
                self.current_user[0]
            )

        )

        print("\nPhone Number Updated Successfully.")


    # Change Password

    @login_required
    @exception_handler
    def change_password(self):

        password = input("Enter New Password : ")

        if not validate_password(password):

            raise ValidationError("Invalid Password")

        password = self.hash_password(password)

        query = """
        UPDATE users
        SET password = ?
        WHERE id = ?
        """

        self.database.execute(

            query,

            (
                password,
                self.current_user[0]
            )

        )

        print("\nPassword Changed Successfully.")


    # Search User

    @exception_handler
    def search_user(self):

        email = input("Enter User Email : ")

        query = """
        SELECT *
        FROM users
        WHERE email = ?
        """

        self.database.execute(

            query,

            (
                email,
            )

        )

        user = self.database.fetch_one()

        if user:

            print_heading("User Found")

            print(f"ID         : {user[0]}")
            print(f"Name       : {user[1]}")
            print(f"Email      : {user[2]}")
            print(f"Role       : {user[4]}")
            print(f"Phone      : {user[5]}")
            print(f"Status     : {user[6]}")

        else:

            print("\nUser Not Found.")


    # Display All Users

    @exception_handler
    def display_users(self):

        query = """
        SELECT *
        FROM users
        ORDER BY id
        """

        self.database.execute(query)

        users = self.database.fetch_all()

        print_heading("All Users")

        if not users:

            print("No Users Found.")

            return

        for user in users:

            print("-" * 70)

            print(f"ID      : {user[0]}")
            print(f"Name    : {user[1]}")
            print(f"Email   : {user[2]}")
            print(f"Role    : {user[4]}")
            print(f"Phone   : {user[5]}")
            print(f"Status  : {user[6]}")
    # Delete User

    @login_required
    @exception_handler
    def delete_user(self):

        choice = input(
            "\nAre you sure you want to delete your account? (Y/N): "
        ).upper()

        if choice != "Y":

            print("Operation Cancelled.")

            return

        query = """
        DELETE FROM users
        WHERE id = ?
        """

        self.database.execute(

            query,

            (
                self.current_user[0],
            )

        )

        print("\nAccount Deleted Successfully.")

        self.current_user = None


    # Activate User

    @exception_handler
    def activate_user(self):

        user_id = input("Enter User ID : ")

        query = """
        UPDATE users
        SET status = ?
        WHERE id = ?
        """

        self.database.execute(

            query,

            (
                "Active",
                user_id
            )

        )

        print("\nUser Activated Successfully.")


    # Deactivate User

    @exception_handler
    def deactivate_user(self):

        user_id = input("Enter User ID : ")

        query = """
        UPDATE users
        SET status = ?
        WHERE id = ?
        """

        self.database.execute(

            query,

            (
                "Inactive",
                user_id
            )

        )

        print("\nUser Deactivated Successfully.")


    # Total Users

    def total_users(self):

        query = """
        SELECT COUNT(*)
        FROM users
        """

        self.database.execute(query)

        total = self.database.fetch_one()

        return total[0]


    # Current Logged-in User

    def get_current_user(self):

        return self.current_user


    # Check Login Status

    def is_logged_in(self):

        return self.current_user is not None


    # Reset Current User

    def reset_current_user(self):

        self.current_user = None


    # Close Database

    def close(self):

        self.database.close()        
