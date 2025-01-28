from models import *
from database import get_db

def login(identificator, password):
    with next(get_db()) as db:
        user = db.query(User).filter_by(
            User.username == identificator,
            User.email == identificator,
            User.phone_number == identificator
        ).first()
        if not user:
            return {'status':0, 'message': 'Аккаунт не найден'}
        elif user.password == password:
            return {'status':1, 'message': 'Вход успешно выполнен'}
        else:
            return {'status':0, 'message': 'Неверный пароль'}
