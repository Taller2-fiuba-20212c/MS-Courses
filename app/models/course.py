from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional, Set
from models.unit import Unit
from models.examModel import ExamModel
from models.consult import Consult

class Course(BaseModel):
    name: str
    description: Optional[str] = Field(None, max_length=300) 
    tags: List[str] = []
    units: List[Unit] = []
    exams: List[ExamModel] = []
    consults: List[Consult] = []
    teachers: List[str] = []
    collaborators: List[str] = []
    students: List[str] = []
    suscriptionIncluded: List[str] = []
    creatorId: str
    creationDate: datetime
    lastModificationDate: datetime