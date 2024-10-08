from hashlib import blake2b

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    password = sa.Column(sa.String(64))
    email = sa.Column(sa.String(50), unique=True)

    def __repr__(self):
        return f'<User {self.email}>'


class Sentence(Base):
    __tablename__ = 'sentences'
    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String(50), unique=True)
    glosa = sa.Column(sa.String(50))
    reviewed = sa.Column(sa.String(50), unique=True)
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)


    def __repr__(self):
        return f'<Sentence {self.text}>'


class UserManagement:
    def __init__(self, engine, salt):
        self._engine = engine
        self._salt = salt.encode("utf8")
    

    def get_hash(self, password):
        hash = blake2b(digest_size=32, salt=self._salt)
        hash.update(password.encode("utf8"))
        return hash.hexdigest()
    
    def verify_password(self, user, password):
        return user.password == self.get_hash(password)
    

    def create_user(self, email, password):
        user = User(email=email, password=self.get_hash(password))
        with Session(self._engine) as session:
            session.add(user)
            session.commit()
        return user
    

    def get_user(self, email):
        with Session(self._engine) as session:
            return session.query(User).filter(User.email == email).first()
    

    def login(self, email, password):
        user = self.get_user(email)
        if user is None:
            return None
        if not self.verify_password(user, password):
            return None
        return user

    def get_user_by_id(self, user_id):
        with Session(self._engine) as session:
            return session.query(User).filter(User.id == user_id).first()
    

    def list_users(self):
        with Session(self._engine) as session:
            return session.query(User).all()
    
    def update_user(self, user):
        with Session(self._engine) as session:
            session.add(user)
            session.commit()