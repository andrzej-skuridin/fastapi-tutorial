from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

# Opening a file with the SQLite database.
# The file will be located at the same directory in the file sql_app.db.
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#PostgreSQL:
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://core:wCh29&HE&T83@localhost/fastapi_tutorial_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
