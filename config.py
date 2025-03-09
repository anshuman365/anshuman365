import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DATABASE_URI = "sqlite:///ni_sql.db"  # Change to PostgreSQL/MySQL for production
    DEBUG = True

config = Config()