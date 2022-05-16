from wg_be_exam.models.base import Base


class IndexResponse(Base):
    base_year: int
    index: float
