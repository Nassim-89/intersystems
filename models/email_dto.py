from typing import List, Union, Optional

from pydantic import BaseModel


class EmailRequest(BaseModel):
    text: str


class EmailResponse(BaseModel):
    id: Optional[int]
    email_from: str
    email_to: str
    subject: str
    message: str

    class Config:
        orm_mode = True
