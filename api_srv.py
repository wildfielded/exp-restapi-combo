#!/usr/bin/python3

import json
import uuid
from time import time

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Session


''' =====----- Global variables -----====='''

# Настройки для SQLAlchemy
DB_PATH = 'sqlite:///sqlite/db.sqlite3'
Base = declarative_base()
ENGINE = sa.create_engine(DB_PATH)
# Время жизни access-token
ACC_TTL = 600.0
# Время жизни refresh-token
REF_TTL = 3600.0


''' =====----- Classes -----===== '''

class User(Base):
    __tablename__ = 'Users'
    uid = sa.Column(sa.String(36), primary_key=True)
    admin = sa.Column(sa.Boolean)
    name = sa.Column(sa.String(1024))
    login = sa.Column(sa.String(1024))
    password = sa.Column(sa.String(1024))
    acc_token = sa.Column(sa.String(36))
    acc_expired = sa.Column(sa.Float)
    ref_token = sa.Column(sa.String(36))
    ref_expired = sa.Column(sa.Float)
    comment = sa.Column(sa.Text(1024))


''' =====----- Decorators -----===== '''


''' =====----- API Methods -----===== '''

def login_post(credentials: dict) -> dict:
    output_dict_ = {'status': 'fail',
                    'text': 'Unknown request'
                   }
    return json.dumps(output_dict_, ensure_ascii=False, indent=2)


#####=====----- THE END -----=====#########################################