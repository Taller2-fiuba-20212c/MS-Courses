from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional
from models.examModel import ExamModel

class Unit(BaseModel):
    name: str
    #PDFS, TEXT or VIDEO
    contentType: str
    #Video: {videoId: xxx}
    #Text: {text: xxx}
    #PDFs: {fileId: xxx}
    content: dict
    exam: Optional[ExamModel] = None
    creatorId: str 
    creationDate: datetime
    lastModificationDate: datetime