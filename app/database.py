from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import psycopg2
#from psycopg2.extras import RealDictCursor
#import time

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:12345678@localhost/fastapi-python'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()

###This is just for record purpose, we are actually connect to the db via sqlalchemy.
### If we connect this way, we can use raw sql with postgresql
# while True:

#    try:
#       conn = psycopg2.connect(host='localhost', database='fastapi-python', user='postgres', password='12345678', cursor_factory=RealDictCursor)
#       cursor = conn.cursor()
#       print("Database connection was succesfull")
#       break
#    except Exception as error:
#       print("Connection to database failed")
#       print("Error: ", error)
#       time.sleep(2)