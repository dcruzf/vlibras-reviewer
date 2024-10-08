from reviewer.models import Base
from reviewer.config import config
from sqlalchemy import create_engine

engine = create_engine(config["DATABASE"])
Base.metadata.create_all(engine)

