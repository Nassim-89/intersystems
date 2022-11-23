import json
from pprint import pprint

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from business.clean import clean_email as custom_clean_email
from database.base_class import Base

from database.sql_database import SessionLocal, engine, db_session
from crud.email_crud import get_email_by_id, save_email
from models.email_dto import EmailResponse, EmailRequest

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/clean_email")
async def clean_email(email_request: EmailRequest):
    email_response = custom_clean_email(email_request.text)
    cleaned_email = save_email(db_session, EmailResponse(**email_response))
    return cleaned_email


@app.get("/emails/{id}")
async def get_email(id: int):
    return get_email_by_id(db_session, id)


if __name__ == '__main__':
    test = """From: 'Mark Twain' <mark.twain@gmail.com>
    To: 'Edgar Allen Poe' <eap@gmail.com>
    Subject: RE:Hello!

    Ed,

    I just read the Tell Tale Heart. You\'ve got problems man.

    Sincerely,
    Marky Mark

    From: 'Edgar Allen Poe' <eap@gmail.com>
    To: 'Mark Twain' <mark.twain@gmail.com>
    Subject: RE: Hello!

    Mark,

    The world is crushing my soul, and so are you.

    Regards,
    Edgar"""
    uvicorn.run(app=app)

