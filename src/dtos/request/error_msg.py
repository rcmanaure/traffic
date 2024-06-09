from pydantic import BaseModel


class ErrorMsgDTO(BaseModel):
    message: str
