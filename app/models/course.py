from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional, Set
from models.unit import Unit
from models.examModel import ExamModel
from models.consult import Consult

class Course(BaseModel):
    name: str
    description: str = Field(None, max_length=300)
    country: str
    category: str 
    tags: List[str] = []
    units: List[Unit] = []
    consults: List[Consult] = []
    teachers: List[str] = []
    collaborators: List[str] = []
    students: List[str] = []
    suscriptionIncluded: List[str] = []
    image: Optional[str]
    published: bool = False
    creatorId: str
    creationDate: datetime
    lastModificationDate: datetime