from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional
from models.examQuestion import ExamQuestion

class Answer(BaseModel):
    question: ExamQuestion
    # Text: {answer: xxx}
    value: dict
    #NULL: sin corregir, OK, WRONG
    state: Optional[str] = None
    grade: Optional[int] = None
    creationDate: datetime
    lastModificationDate: datetime