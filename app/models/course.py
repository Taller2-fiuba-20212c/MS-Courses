<<<<<<< HEAD:models/course.py
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
    image: Optional[str]
    published: bool = False
    creatorId: str
    creationDate: datetime
=======
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
>>>>>>> d32b9d5f19d73edb785fba18625182b9f8f10349:app/models/course.py
    lastModificationDate: datetime