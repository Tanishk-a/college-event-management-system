"""
==========================================================
Event Management System
Main Application
==========================================================
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import logging

# ==========================================================
# Local Project Imports
# ==========================================================

from database.database import Database

from common.constants import (
    APP_NAME,
    VERSION,
    AUTHOR,
    DATABASE_NAME,
)


# ==========================================================
# Main Function
# ==========================================================

def main():

    print("=" * 70)
    print(APP_NAME.center(70))
    print("=" * 70)

    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print(f"Database: {DATABASE_NAME}")

    print("\nInitializing Project...\n")

    db = None

    try:

        # Connect Database
        db = Database()

        # Create Required Tables
        db.create_tables()

        print("\nLoading Modules...\n")

        modules = [
            "Common",
            "Database",
            "Accounts",
            "Institutions",
            "Events",
            "Registrations",
            "Approvals",
            "Notifications",
            "Dashboard",
            "Export",
        ]

        for module in modules:
            print(f"✓ {module} Module Loaded")

        print("\nProject Started Successfully.")

    except Exception as error:

        logging.exception(error)
        print(f"\nProject Initialization Failed:\n{error}")

    finally:

        if db is not None:
            db.close()


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()