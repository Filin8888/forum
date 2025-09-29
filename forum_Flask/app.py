from flask import Flask
from config import Config
from flask_login import LoginManager
from extentios import db
from admin import init_admin

login_manager = LoginManager()  # створюємо менеджер логіну


def create_app():
    app = Flask(__name__)                   # створюємо Flask-додаток
    app.config.from_object(Config)          # завантажуємо налаштування з config.py
    db.init_app(app)                        # прив’язуємо SQLAlchemy до Flask

    login_manager.init_app(app)             # прив'язуємо до Flask
    login_manager.login_view = "main.login" # маршрут для редиректу, якщо не залогінений

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # реєструємо маршрути
    from routes import main_bp
    app.register_blueprint(main_bp)

    # створюємо таблиці
    with app.app_context():
        db.create_all()

    # підключаємо адмінку
    init_admin(app)



    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
