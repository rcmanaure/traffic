from pathlib import Path

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from src.config.settings import settings


class Mailer:
    def __init__(self, username: str, password: str, port: int, host: str):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=username,
            MAIL_PASSWORD=password,
            MAIL_FROM=username,
            MAIL_PORT=port,
            MAIL_SERVER=host,
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            TEMPLATE_FOLDER=Path(__file__).parent.parent / "EMAIL_TEMPLATES",
        )
        self.username = username

    async def send_msg_as_html(self, to, subject, body, template_name):
        message = MessageSchema(
            subject=subject, recipients=[to], template_body=body, subtype="html"
        )
        fm = FastMail(self.conf)
        await fm.send_message(message, template_name=template_name)


def get_mailer():
    return Mailer(
        username=settings.MAIL_USERNAME,
        password=settings.MAIL_PASSWORD,
        port=settings.MAIL_PORT,
        host=settings.MAIL_HOST,
    )
