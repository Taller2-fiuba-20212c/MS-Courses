from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional
from models.image import Image

class ExamQuestion(BaseModel):
    #TEXT
    questionType: str
    # Text: {question: xxx}
    question: object 
    creationDate: datetime
    lastModificationDate: datetime