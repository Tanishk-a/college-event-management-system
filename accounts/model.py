"""
Event Management System
Accounts Models
"""

# Standard Library Imports

from datetime import datetime
from uuid import uuid4

# Local Project Imports

from common.constants import *


class User:

    def __init__(
        self,
        name,
        email,
        password,
        role,
        phone,
        status="Active"
    ):

        self.user_id = str(uuid4())

        self.name = name

        self.email = email

        self.password = password

        self.role = role

        self.phone = phone

        self.status = status

        self.created_at = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    def activate(self):

        self.status = "Active"

    def deactivate(self):

        self.status = "Inactive"

    def display(self):

        print("\nUser Information")
        print("-" * 40)

        print(f"User ID      : {self.user_id}")
        print(f"Name         : {self.name}")
        print(f"Email        : {self.email}")
        print(f"Role         : {self.role}")
        print(f"Phone        : {self.phone}")
        print(f"Status       : {self.status}")
        print(f"Created At   : {self.created_at}")

    def __str__(self):

        return f"{self.name} ({self.role})"


class StudentProfile:

    def __init__(
        self,
        user,
        enrollment_number,
        department,
        semester,
        course
    ):

        self.user = user

        self.enrollment_number = enrollment_number

        self.department = department

        self.semester = semester

        self.course = course

    def display(self):

        self.user.display()

        print(f"Enrollment   : {self.enrollment_number}")
        print(f"Department   : {self.department}")
        print(f"Semester     : {self.semester}")
        print(f"Course       : {self.course}")

    def __str__(self):

        return self.user.name


class StaffProfile:

    def __init__(
        self,
        user,
        employee_id,
        designation,
        department
    ):

        self.user = user

        self.employee_id = employee_id

        self.designation = designation

        self.department = department

    def display(self):

        self.user.display()

        print(f"Employee ID  : {self.employee_id}")
        print(f"Designation  : {self.designation}")
        print(f"Department   : {self.department}")

    def __str__(self):

        return self.user.name


class AdminProfile:

    def __init__(
        self,
        user
    ):

        self.user = user

    def display(self):

        self.user.display()

        print("Administrator Account")

    def __str__(self):

        return self.user.name


class CoordinatorProfile:

    def __init__(
        self,
        user,
        club_name
    ):

        self.user = user

        self.club_name = club_name

    def display(self):

        self.user.display()

        print(f"Club Name    : {self.club_name}")

    def __str__(self):

        return self.user.name


class RegistrarProfile:

    def __init__(
        self,
        user,
        office
    ):

        self.user = user

        self.office = office

    def display(self):

        self.user.display()

        print(f"Office       : {self.office}")

    def __str__(self):

        return self.user.name
