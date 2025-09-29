# create_demo_users.py
from app import create_app
from extentios import db
from models import User
import random

demo_users = [
    # admin
    {"username":"admin", "email":"admin@example.com", "password":"admin123", "role":"admin"},
    # moderators (2)
    {"username":"mod_alex", "email":"mod.alex@example.com", "password":"modpass1", "role":"moderator"},
    {"username":"mod_ira", "email":"mod.ira@example.com", "password":"modpass2", "role":"moderator"},
]

# ~20 regular users (add more names as needed)
names = [
"ivan","oleg","sergiy","yaroslav","dmytro","andriy","pavlo","marta","olena","katya",
"natalia","viktor","taras","ksenia","igor","roman","petro","sasha","natasha","max"
]
for n in names:
    demo_users.append({
        "username": f"{n}",
        "email": f"{n}@example.com",
        "password": "user1234",
        "role": "user"
    })

def main():
    app = create_app()
    with app.app_context():
        # optional: drop/create tables if you want clean demo (CAREFUL)
        # db.drop_all()
        # db.create_all()

        created = 0
        for u in demo_users:
            exists = User.query.filter_by(username=u["username"]).first()
            if exists:
                print(f"skip {u['username']} (exists)")
                continue
            user = User(username=u["username"], email=u["email"], role=u["role"])
            user.set_password(u["password"])
            db.session.add(user)
            created += 1
        db.session.commit()
        print(f"Created {created} demo users. Login admin: admin/admin123")

if __name__ == "__main__":
    main()
