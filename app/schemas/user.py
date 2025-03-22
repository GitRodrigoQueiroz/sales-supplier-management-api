import re

from pydantic import BaseModel, validator


class User(BaseModel):
    user_name: str
    password: str

    @validator("user_name")
    def validate_username(cls, value):
        if not re.match("^([a-z]|[0-9])+$", value):
            raise ValueError("Username format invalid")
        return value
