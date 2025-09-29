# налаштування підключення до БД
import os


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin123@localhost:5432/forum_base"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev_secret"

