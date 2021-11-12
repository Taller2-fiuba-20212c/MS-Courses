from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional

class Course(BaseModel):
    name: str
    description: Optional[str] = Field(None, max_length=300) 
    price: float = Field(gt=0)
    tags: List[str] = []
    units: List[Unit] = []
    exams: List[ExamModel] = []
    consults: List[Consult] = []
    teachers: List[str] = []
    colaborators: List[str] = []
    students: List[str] = []
    creatorId: str
    creationDate: datetime
    lastModificationDate: datetime