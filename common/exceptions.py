"""
Event Management System
Custom Exceptions
"""


# Base Exception

class EventManagementError(Exception):
    """Base exception for the Event Management System."""
    pass


# Database Exceptions

class DatabaseConnectionError(EventManagementError):
    """Raised when database connection fails."""
    pass


class DatabaseQueryError(EventManagementError):
    """Raised when a database query fails."""
    pass


# Authentication Exceptions

class AuthenticationError(EventManagementError):
    """Raised when authentication fails."""
    pass


class InvalidCredentialsError(AuthenticationError):
    """Raised for invalid email or password."""
    pass


class UserNotFoundError(AuthenticationError):
    """Raised when a user is not found."""
    pass


class AccountLockedError(AuthenticationError):
    """Raised when an account is locked."""
    pass


# Authorization Exceptions

class AuthorizationError(EventManagementError):
    """Raised when user lacks permission."""
    pass


class PermissionDeniedError(AuthorizationError):
    """Raised when access is denied."""
    pass


# Validation Exceptions

class ValidationError(EventManagementError):
    """Raised when validation fails."""
    pass


class InvalidEmailError(ValidationError):
    """Raised for invalid email address."""
    pass


class InvalidPasswordError(ValidationError):
    """Raised for invalid password."""
    pass


class InvalidPhoneNumberError(ValidationError):
    """Raised for invalid phone number."""
    pass


# Event Exceptions

class EventError(EventManagementError):
    """Base event exception."""
    pass


class EventNotFoundError(EventError):
    """Raised when an event is not found."""
    pass


class EventCapacityError(EventError):
    """Raised when event capacity is exceeded."""
    pass


class EventAlreadyExistsError(EventError):
    """Raised when an event already exists."""
    pass


# Registration Exceptions

class RegistrationError(EventManagementError):
    """Base registration exception."""
    pass


class DuplicateRegistrationError(RegistrationError):
    """Raised when a user registers twice."""
    pass


class RegistrationClosedError(RegistrationError):
    """Raised when registration is closed."""
    pass


# Approval Exceptions

class ApprovalError(EventManagementError):
    """Base approval exception."""
    pass


class ApprovalDeniedError(ApprovalError):
    """Raised when approval is denied."""
    pass


class ApprovalPendingError(ApprovalError):
    """Raised when approval is still pending."""
    pass


# Notification Exceptions

class NotificationError(EventManagementError):
    """Base notification exception."""
    pass


class EmailSendError(NotificationError):
    """Raised when email sending fails."""
    pass


# Export Exceptions

class ExportError(EventManagementError):
    """Base export exception."""
    pass


class ExcelExportError(ExportError):
    """Raised when Excel export fails."""
    pass


class PDFExportError(ExportError):
    """Raised when PDF export fails."""
    pass


# File Exceptions

class FileError(EventManagementError):
    """Base file exception."""
    pass


class FileNotFoundError(FileError):
    """Raised when a file is not found."""
    pass


class InvalidFileFormatError(FileError):
    """Raised when an unsupported file format is used."""
    pass


# End of File
