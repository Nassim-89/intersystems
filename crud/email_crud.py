from sqlalchemy.orm import Session

from models import email, email_dto
from models.email import Email


def get_email_by_id(db: Session, mail_id: int):
    return db.query(email.Email).filter(email.Email.id == mail_id).first()


def save_email(db: Session, mail: email_dto.EmailResponse):
    converted_mail = Email(email_from=mail.email_from, email_to=mail.email_to, subject=mail.subject,
                           message=mail.message)
    db.add(converted_mail)
    db.commit()
    db.refresh(converted_mail)
    return converted_mail
