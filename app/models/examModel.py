from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional
from models.examQuestion import ExamQuestion
from models.examResolution import ExamResolution

class ExamModel(BaseModel):
    name: str
    description: Optional[str] = Field(None, max_length=300) 
    examQuestions: List[ExamQuestion] = []
    examResolutions: List[ExamResolution] = []
    #CREATED, PUBLISHED, CLOSED
    state: str
    creatorId: str
    creationDate: datetime
    lastModificationDate: datetime