from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import config
from models import Base 

engine = create_engine(config.DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    
def execute_query(query):
    try:
        result = session.execute(text(query))
        session.commit()
        return result.fetchall()
    except Exception as e:
        return str(e)
       