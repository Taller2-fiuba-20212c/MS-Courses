from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date
from typing import List, Optional

class Unit(BaseModel):
    name: str
    #PDFS, TEXT or VIDEO
    contentType: str
    #Video: {videoId: xxx}
    #Text: {text: xxx}
    #PDFs: {fileId: xxx}
    content: object
    creatorId: str 
    creationDate: datetime
    lastModificationDate: datetime