from pydantic import BaseModel
from datetime import date
from typing import Optional


class TripCreate(BaseModel):
    title: str
    destination: str
    start_date: date
    end_date: date
    description: Optional[str] = None


class TripUpdate(BaseModel):
    title: Optional[str] = None
    destination: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None


class TripResponse(BaseModel):
    id: int
    title: str
    destination: str
    start_date: date
    end_date: date
    description: Optional[str]
    user_id: int

    class Config:
        from_attributes = True