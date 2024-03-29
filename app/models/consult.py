from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional

class Consult(BaseModel):
    question: str
    response: Optional[str] = None
    creatorId: str
    teacherId: str
    creationDate: datetime
    lastModificationDate: datetime