from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import INTEGER

from database.base_class import Base


class Email(Base):
    id = Column(INTEGER, primary_key=True, index=True)
    email_from = Column(String)
    email_to = Column(String)
    subject = Column(String)
    message = Column(String)
