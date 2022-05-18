from fastapi import APIRouter, HTTPException
from fastapi.requests import Request

from wg_be_exam.actions.getHealthIndex import GetHealthIndex
from wg_be_exam.config import Config
from wg_be_exam.routes.index.models import IndexResponse

"""
# 1.1
Make sure only 1996, 2004 and 2013 are valid
https://fastapi.tiangolo.com/tutorial/handling-errors/
Tip: from fastapi import HTTPException

# 1.2
Retrieve the latest index from external source for given base year
https://statbel.fgov.be/en/themes/consumer-prices/health-index
Tip: Although not that trivial to find, it's possible to retrieve the health-index as a JSON response (check Network tab). This can probably save you some work!

# 1.3
# Format and return the response
"""


def get_index_router():
    router = APIRouter()

    @router.get("/index", response_model=IndexResponse)
    async def get_health_index(request: Request, year: int = 2004) -> IndexResponse:
        if year not in [1996, 2004, 2013]:
            raise HTTPException(
                status_code=404, detail=f'Year {year} is not valid')

        index = GetHealthIndex.handle(Config().URL_HEALT_INDEXES, year)

        return IndexResponse(base_year=year, index=index)

    return router
