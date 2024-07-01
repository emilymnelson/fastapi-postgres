# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import engine, AsyncSessionLocal
from app.models import Base, CME
from app.schemas import CMESchema
from sqlalchemy.future import select
import uvicorn

app = FastAPI()

# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Default endpoint for /cme/
@app.get("/cme/", response_model=list[CMESchema])
async def get_all_cme_records(db: Session = Depends(get_db)):
    result = await db.execute(select(CME))
    return result.scalars().all()

# API endpoint to fetch CME records filtered by year
@app.get("/cme/{year}", response_model=list[CMESchema])
async def get_cme_records(year: str, db: Session = Depends(get_db)):
    result = await db.execute(select(CME).where(CME.year == year))
    return result.scalars().all()

# Run the application with Uvicorn
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
