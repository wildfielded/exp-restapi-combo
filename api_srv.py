#!/usr/bin/python3

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Session


''' =====----- Global variables -----====='''

# Настройки для SQLAlchemy
DB_PATH = 'sqlite:///sqlite/db.sqlite3'
Base = declarative_base()
ENGINE = sa.create_engine(DB_PATH)


''' =====----- Classes -----===== '''

class User(Base):
    __tablename__ = 'Users'


''' =====----- Decorators -----===== '''

''' =====----- API Methods -----===== '''

#####=====----- THE END -----=====#########################################