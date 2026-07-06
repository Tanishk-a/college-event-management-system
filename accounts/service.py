from database.database import Database
from common.constants import DATABASE_NAME


def register_user(name, email, password, role, phone):
    db = Database()
    try:
        db.execute(
            "INSERT INTO users(name, email, password, role, phone, status, created_at) VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
            (name, email, password, role, phone, "active"),
        )
        user = db.fetch_one("SELECT id, name, email, role, phone, status FROM users WHERE email = ?", (email,))
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


def authenticate_user(email, password):
    db = Database()
    try:
        user = db.fetch_one("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))
        return user is not None
    finally:
        db.close()
