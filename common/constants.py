"""
==========================================================
Event Management System
Project Constants
==========================================================
"""

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "Event Management System"
VERSION = "1.0.0"
AUTHOR = "Tanishka"

# ==========================================================
# Database Configuration
# ==========================================================

DATABASE_NAME = "event_management.db"

# ==========================================================
# User Roles
# ==========================================================

ADMIN = "Admin"
STUDENT = "Student"
FACULTY = "Faculty"
COORDINATOR = "Coordinator"
REGISTRAR = "Registrar"

ROLES = [
    ADMIN,
    STUDENT,
    FACULTY,
    COORDINATOR,
    REGISTRAR
]

# ==========================================================
# Event Status
# ==========================================================

PENDING = "Pending"
APPROVED = "Approved"
REJECTED = "Rejected"
SENT_BACK = "Sent Back"
COMPLETED = "Completed"
CANCELLED = "Cancelled"

EVENT_STATUS = [
    PENDING,
    APPROVED,
    REJECTED,
    SENT_BACK,
    COMPLETED,
    CANCELLED
]

# ==========================================================
# Registration Status
# ==========================================================

REGISTERED = "Registered"
WAITING = "Waiting"
ACCEPTED = "Accepted"
REJECTED_REGISTRATION = "Rejected"

REGISTRATION_STATUS = [
    REGISTERED,
    WAITING,
    ACCEPTED,
    REJECTED_REGISTRATION
]

# ==========================================================
# Approval Levels
# ==========================================================

LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

# ==========================================================
# Default Values
# ==========================================================

MAX_EVENT_CAPACITY = 100
MIN_EVENT_CAPACITY = 1

MAX_LOGIN_ATTEMPTS = 3

DEFAULT_PASSWORD_LENGTH = 8

DEFAULT_COUNTRY = "India"

DEFAULT_TIMEZONE = "Asia/Kolkata"

DEFAULT_DATE_FORMAT = "%d-%m-%Y"

DEFAULT_TIME_FORMAT = "%H:%M:%S"

DEFAULT_DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"

# ==========================================================
# File Names
# ==========================================================

EVENT_EXPORT_FILE = "events.xlsx"

REGISTRATION_EXPORT_FILE = "registrations.xlsx"

USER_EXPORT_FILE = "users.xlsx"

LOG_FILE = "event_management.log"

# ==========================================================
# Messages
# ==========================================================

LOGIN_SUCCESS = "Login Successful"

LOGIN_FAILED = "Invalid Email or Password"

REGISTRATION_SUCCESS = "Registration Successful"

EVENT_CREATED = "Event Created Successfully"

EVENT_UPDATED = "Event Updated Successfully"

EVENT_DELETED = "Event Deleted Successfully"

DATABASE_CONNECTED = "Database Connected Successfully"

DATABASE_CLOSED = "Database Connection Closed"

INVALID_CHOICE = "Invalid Choice"

ACCESS_DENIED = "Access Denied"

# ==========================================================
# End of Constants
# ==========================================================
