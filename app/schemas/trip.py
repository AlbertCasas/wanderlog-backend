from pydantic import BaseModel, field_validator
from pydantic import BaseModel
from datetime import date
from typing import Optional


class TripCreate(BaseModel):
    title: str
    destination: str
    start_date: date
    end_date: date
    description: Optional[str] = None

    @field_validator('end_date')
    @classmethod
    def end_date_after_start(cls, v, info):
        if 'start_date' in info.data and v < info.data['start_date']:
            raise ValueError('end_date must be after start_date')
        return v


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