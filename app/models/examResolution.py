from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional
from models.answer import Answer

class ExamResolution(BaseModel):
    answers: List[Answer] = []
    grade: Optional[int]
    #APPROVED, DISAPPROVED 
    state: Optional[str]
    creatorId: str
    creationDate: datetime
    lastModificationDate: datetime