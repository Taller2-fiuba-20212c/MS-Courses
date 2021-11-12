from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional

class ExamAnswer(BaseModel):
    answers: List[Answer] = []
    grade: Optional[int]
    #APPROVED, DISAPPROVED 
    state: Optional[str]
    creatorId: str
    creationDate: datetime
    lastModificationDate: datetime