from pydantic import BaseModel
from .status import Status


class Member(BaseModel):
    id: str
    name: str
    surname: str
    status: Status
    mail: str
