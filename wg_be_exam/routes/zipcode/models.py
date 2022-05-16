from typing import Optional

from wg_be_exam.models.base import Base


class Zipcode(Base):
    zipcode: int
    risk_factor: Optional[str] = None


class ZipcodeResponse(Zipcode):
    exists: bool = False
