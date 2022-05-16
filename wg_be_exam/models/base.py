from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        table = ""
        use_enum_values = True
        anystr_strip_whitespace = True
        validate_all = True
        validate_assignment = True
        extra = "forbid"
        arbitrary_types_allowed = True
