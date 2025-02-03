from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
# Load database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("Error: DATABASE_URL environment variable is not set. Ensure it is configured before running the application.")

# Create the database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # Keeping this for security clarity
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(20), nullable=False, default="user")
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

# Dependency Injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
