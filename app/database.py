#required imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#required database URL
username = os.getenv('codeblog_username')
password = os.getenv('codeblog_password')
hostname = os.getenv('codeblog_hostname')
database = os.getenv('codeblog_database')

database_url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'

SQLALCHEMY_DATABASE_URL = database_url

#create a engine that responsible for connect sqlalchemy with postgresql database
Engine = create_engine(SQLALCHEMY_DATABASE_URL)

#create a session and bind engine with it
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

#a base class, this class will inherit by model classes who wants to connect with database
Base = declarative_base()

#this create/established a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()