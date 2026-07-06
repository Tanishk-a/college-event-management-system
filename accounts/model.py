"""
==========================================================
Event Management System
Accounts Models
==========================================================
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

from datetime import datetime
from uuid import uuid4

# ==========================================================
# Local Imports
# ==========================================================

from common.constants import *

# ==========================================================
# User Model
# ==========================================================

class User:

    def __init__(
        self,
        name,
        email,
        password,
        role,
        phone
    ):

        self.user_id = str(uuid4())

        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.phone = phone

        self.is_active = True

        self.created_at = datetime.now()

    # ------------------------------------------------------

    def display(self):

        print("\n========== USER DETAILS ==========")
        print(f"User ID     : {self.user_id}")
        print(f"Name        : {self.name}")
        print(f"Email       : {self.email}")
        print(f"Role        : {self.role}")
        print(f"Phone       : {self.phone}")
        print(f"Status      : {'Active' if self.is_active else 'Inactive'}")
        print(f"Created At  : {self.created_at}")

    # ------------------------------------------------------

    def activate(self):

        self.is_active = True

    # ------------------------------------------------------

    def deactivate(self):

        self.is_active = False

    # ------------------------------------------------------

    def __str__(self):

        return f"{self.name} ({self.role})"


# ==========================================================
# Student Profile
# ==========================================================

class StudentProfile:

    def __init__(
        self,
        user,
        enrollment_no,
        department,
        semester,
        course
    ):

        self.user = user

        self.enrollment_no = enrollment_no
        self.department = department
        self.semester = semester
        self.course = course

    # ------------------------------------------------------

    def display(self):

        print("\n========== STUDENT PROFILE ==========")

        self.user.display()

        print(f"Enrollment  : {self.enrollment_no}")
        print(f"Department  : {self.department}")
        print(f"Semester    : {self.semester}")
        print(f"Course      : {self.course}")


# ==========================================================
# Staff Profile
# ==========================================================

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

    # ------------------------------------------------------

    def display(self):

        print("\n========== STAFF PROFILE ==========")

        self.user.display()

        print(f"Employee ID : {self.employee_id}")
        print(f"Designation : {self.designation}")
        print(f"Department  : {self.department}")