from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional

class ExamQuestion(BaseModel):
    #TEXT
    questionType: str
    # Text: {question: xxx}
    question: dict 
    creationDate: datetime
    lastModificationDate: datetime