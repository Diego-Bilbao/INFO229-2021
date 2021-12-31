from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date

class News(BaseModel):
    id: int
    title: str
    date: date 
    url: str
    media_outlet: str 
    category: str
    class Config:
        orm_mode = True

