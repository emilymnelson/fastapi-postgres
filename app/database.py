# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:pw@localhost/postgres"

# Async SQLAlchemy engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# Async sessionmaker
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
