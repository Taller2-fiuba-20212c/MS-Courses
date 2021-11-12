from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional

class Answer(BaseModel):
    question: ExamQuestion
    # Text: {answer: xxx}
    value: object
    #NULL: sin corregir, OK, WRONG
    state: Optional[str]
    creationDate: datetime
    lastModificationDate: datetime