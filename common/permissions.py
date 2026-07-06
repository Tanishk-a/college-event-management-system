"""
Event Management System
Permission Functions
"""

from common.constants import *


# User Role Permissions

def is_admin(role):
    """Check if the user is an Admin."""

    return role == ADMIN


def is_student(role):
    """Check if the user is a Student."""

    return role == STUDENT


def is_faculty(role):
    """Check if the user is a Faculty member."""

    return role == FACULTY


def is_coordinator(role):
    """Check if the user is a Coordinator."""

    return role == COORDINATOR


def is_registrar(role):
    """Check if the user is a Registrar."""

    return role == REGISTRAR


# Event Permissions

def can_create_event(role):
    """Permission to create an event."""

    return role in [ADMIN, COORDINATOR]


def can_edit_event(role):
    """Permission to edit an event."""

    return role in [ADMIN, COORDINATOR]


def can_delete_event(role):
    """Permission to delete an event."""

    return role == ADMIN


def can_view_events(role):
    """Permission to view events."""

    return role in ROLES


# Registration Permissions

def can_register_event(role):
    """Permission to register for an event."""

    return role == STUDENT


def can_cancel_registration(role):
    """Permission to cancel registration."""

    return role == STUDENT


# Approval Permissions

def can_approve_event(role):
    """Permission to approve events."""

    return role in [FACULTY, REGISTRAR, ADMIN]


def can_reject_event(role):
    """Permission to reject events."""

    return role in [FACULTY, REGISTRAR, ADMIN]


# Dashboard Permissions

def can_view_dashboard(role):
    """Permission to access dashboard."""

    return role in ROLES


# Export Permissions

def can_export_reports(role):
    """Permission to export reports."""

    return role in [ADMIN, REGISTRAR]


# Notification Permissions

def can_send_notifications(role):
    """Permission to send notifications."""

    return role in [ADMIN, COORDINATOR]


# Account Permissions

def can_manage_users(role):
    """Permission to manage user accounts."""

    return role == ADMIN


def can_manage_institutions(role):
    """Permission to manage institutions."""

    return role == ADMIN


# General Permission

def has_permission(role):
    """Check if role is valid."""

    return role in ROLES


# End of File
