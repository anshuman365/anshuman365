from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import config

engine = create_engine(config.DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def execute_query(query):
    try:
        result = session.execute(text(query))
        session.commit()
        return result.fetchall()
    except Exception as e:
        return str(e)