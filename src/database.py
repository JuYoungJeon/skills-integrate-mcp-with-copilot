"""
Database configuration and models for the High School Management System
"""

from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from pathlib import Path

# Database URL - use SQLite for simplicity
DATABASE_URL = "sqlite:///./mergington_activities.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


class Activity(Base):
    """Activity model for database storage"""
    __tablename__ = "activities"

    name = Column(String, primary_key=True, index=True)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Participant(Base):
    """Participant model to track student signups"""
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    activity_name = Column(String, index=True)
    email = Column(String, index=True)
    signed_up_at = Column(DateTime, default=datetime.utcnow)


def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
