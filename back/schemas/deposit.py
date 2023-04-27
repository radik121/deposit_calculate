from datetime import datetime
from pydantic import BaseModel, validator, Field


class DepositModels(BaseModel):
    date: str
    periods: int = Field(ge=1, le=60)
    amount: int = Field(ge=10_000, le=3_000_000)
    rate: int = Field(ge=1, le=8)

    class Config:
        schema_extra = {
            "example": {
                "date": "31.01.2023",
                "periods": 6,
                "amount": 10000,
                "rate": 6,
            },
        }

    @validator('date')
    def check_date(cls, v):
        date = datetime.strptime(v, '%d.%m.%Y').date()
        if not date:
            raise ValueError('The date must be in the format dd.mm.YYYY')
        return date