"""
Event Management System
Account Services
"""

import hashlib

from database.database import Database
from common.constants import *
from common.validators import *


# Register User

def register_user(name, email, password, role, phone):

    if not validate_name(name):
        raise ValueError("Invalid Name")

    if not validate_email(email):
        raise ValueError("Invalid Email")

    if not validate_password(password):
        raise ValueError("Invalid Password")

    if not validate_phone(phone):
        raise ValueError("Invalid Phone Number")

    db = Database()

    try:

        encrypted_password = hashlib.sha256(
            password.encode()
        ).hexdigest()

        db.execute(
            """
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
            (?, ?, ?, ?, ?, ?, datetime('now'))
            """,
            (
                name,
                email,
                encrypted_password,
                role,
                phone,
                "Active"
            ),
        )

        user = db.fetch_one(
            """
            SELECT
                id,
                name,
                email,
                role,
                phone,
                status
            FROM users
            WHERE email = ?
            """,
            (email,),
        )

        return {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "role": user[3],
            "phone": user[4],
            "status": user[5],
        }

    finally:

        db.close()


# Login User

def authenticate_user(email, password):

    db = Database()

    try:

        encrypted_password = hashlib.sha256(
            password.encode()
        ).hexdigest()

        user = db.fetch_one(
            """
            SELECT *
            FROM users
            WHERE email = ?
            AND password = ?
            """,
            (
                email,
                encrypted_password
            ),
        )

        return user

    finally:

        db.close()


# Get User

def get_user(email):

    db = Database()

    try:

        return db.fetch_one(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,
            (email,),
        )

    finally:

        db.close()


# Get All Users

def get_all_users():

    db = Database()

    try:

        return db.fetch_all(
            """
            SELECT *
            FROM users
            """
        )

    finally:

        db.close()


# Update Phone Number

def update_phone(email, phone):

    db = Database()

    try:

        db.execute(
            """
            UPDATE users
            SET phone = ?
            WHERE email = ?
            """,
            (
                phone,
                email
            ),
        )

    finally:

        db.close()


# Change Password

def change_password(email, password):

    db = Database()

    try:

        encrypted_password = hashlib.sha256(
            password.encode()
        ).hexdigest()

        db.execute(
            """
            UPDATE users
            SET password = ?
            WHERE email = ?
            """,
            (
                encrypted_password,
                email
            ),
        )

    finally:

        db.close()


# Delete User

def delete_user(email):

    db = Database()

    try:

        db.execute(
            """
            DELETE FROM users
            WHERE email = ?
            """,
            (email,),
        )

    finally:

        db.close()
