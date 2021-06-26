from .models import Users
from app import db
from werkzeug.security import generate_password_hash


def create_new_user(username,password):
    hash_password = generate_password_hash(password=password, method='sha256')
    new_user = Users(username=username, password=hash_password)
    db.session.add(new_user)
    db.session.commit()
    return True