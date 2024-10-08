

from reviewer.models import UserManagement
from reviewer.config import config 
from sqlalchemy import create_engine

def add_user_to_session(session, user=None):
    if "user" not in session:
        session.user = None
    if "user_manager" not in session:
        engine = create_engine(config["DATABASE"])
        session.user_manager = UserManagement(engine, salt=config["SALT"])