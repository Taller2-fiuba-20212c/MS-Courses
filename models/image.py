from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

class Image(BaseModel):
    url: HttpUrl
    name: str