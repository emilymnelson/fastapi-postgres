# schemas.py
from pydantic import BaseModel

class CMESchema(BaseModel):
    id: int
    year: str
    specialty: str
    hospital: str

    class Config:
        orm_mode = True
