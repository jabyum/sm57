from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# указываем тип и название базы данных
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/social_media'
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
# создаем движок нашей базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# создание функцию для создания сессий
SessionLocal = sessionmaker(bind=engine)
# создаем суперкласс для моделей (будет его наследовать как Models в джанго)
Base = declarative_base()

# создание функции-генератора сессий
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()