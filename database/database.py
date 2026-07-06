"""
==========================================================
Event Management System
Database Manager
==========================================================
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import sqlite3

# ==========================================================
# Local Project Imports
# ==========================================================

from common.constants import DATABASE_NAME


# ==========================================================
# Database Class
# ==========================================================

class Database:

    def __init__(self):

        try:
            self.connection = sqlite3.connect(DATABASE_NAME)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()

            print("✓ Database Connected Successfully")

        except sqlite3.Error as error:
            print(f"Database Connection Error: {error}")
            self.connection = None
            self.cursor = None

    # ======================================================
    # Execute Query (INSERT, UPDATE, DELETE)
    # ======================================================

    def execute(self, query, values=()):

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True

        except sqlite3.Error as error:
            print(f"Database Error: {error}")
            return False

    # ======================================================
    # Fetch One Record
    # ======================================================

    def fetch_one(self, query, values=()):

        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchone()

        except sqlite3.Error as error:
            print(f"Database Error: {error}")
            return None

    # ======================================================
    # Fetch All Records
    # ======================================================

    def fetch_all(self, query, values=()):

        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()

        except sqlite3.Error as error:
            print(f"Database Error: {error}")
            return []

    # ======================================================
    # Create Tables
    # ======================================================

    def create_tables(self):

        try:

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(

                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL,
                    phone TEXT,
                    status TEXT,
                    created_at TEXT

                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS events(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    location TEXT NOT NULL,
                    event_date TEXT NOT NULL,
                    description TEXT,
                    created_at TEXT
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS registrations(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    event_id INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(event_id) REFERENCES events(id)
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS approvals(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    registration_id INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    approved_at TEXT,
                    FOREIGN KEY(registration_id) REFERENCES registrations(id)
                )
            """)

            self.connection.commit()

            print("✓ Core Tables Created Successfully")

        except sqlite3.Error as error:

            print(f"Table Creation Error: {error}")

    # ======================================================
    # Commit Changes
    # ======================================================

    def commit(self):

        if self.connection:
            self.connection.commit()

    # ======================================================
    # Rollback
    # ======================================================

    def rollback(self):

        if self.connection:
            self.connection.rollback()

    # ======================================================
    # Close Database
    # ======================================================

    def close(self):

        try:
            if self.connection:
                self.connection.close()
                print("✓ Database Connection Closed")

        except sqlite3.Error as error:
            print(f"Close Error: {error}")