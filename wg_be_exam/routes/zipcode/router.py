import psycopg2
import asyncio
from databases import Database
from fastapi import APIRouter, Query, HTTPException, Depends
from fastapi.requests import Request

from wg_be_exam.config import Config
from wg_be_exam.routes.zipcode.models import ZipcodeResponse
from wg_be_exam.actions.readCsv import ReadCsv

# Dependency
async def get_db():
    db = Database(Config().DB_DSN.get_secret_value())
    await db.connect()
    try:
        yield db
    finally:
        await db.disconnect()

def get_zipcode_router():
    router = APIRouter()

    """
    # 2.1
    Validate if the zipcode entered has the correct format
    (integer between 1000 and 9999)

    # 2.2
    Read the file zipcodes.csv and format data

    # 2.3
    Validate if the zipcode entered is in the dataset

    # 2.4
    Formulate appropriate response
    """

    @router.get("/zipcodes/{zipcode}", response_model=ZipcodeResponse)
    async def get_zipcode_risk_factor(request: Request, zipcode: int) -> ZipcodeResponse:
        # Add your solution here

        if zipcode < 1000 or zipcode > 9999:
            raise HTTPException(status_code=404, detail=f'Zipcode {str(zipcode)} is not valid')  # nopep8

        df_zipcodes = ReadCsv().handle('zipcodes.csv')

        if zipcode in df_zipcodes.index.to_list():
            return ZipcodeResponse(
                zipcode=zipcode,
                risk_factor=df_zipcodes[df_zipcodes.index == zipcode]['risk_factor'].values[0],  # nopep8
                exists=True
            )

        return ZipcodeResponse(
            zipcode=zipcode
        )

    """
    # 3.1
    Retrieve the risk factor for a zipcode from the database.
    The route should return the risk factor for a given zipcode.
    """

    @router.get("/databases/zipcodes/{zipcode}", response_model=ZipcodeResponse)
    async def get_zipcode_risk_factor_from_database(request: Request, zipcode: int, db: Database = Depends(get_db)) -> ZipcodeResponse:
        query = "SELECT * FROM zipcodes WHERE zipcode = :zipcode"
        select_zipcode_task = asyncio.create_task(db.fetch_one(query=query, values={"zipcode": zipcode}))  # nopep8
        requested_zipcode = await select_zipcode_task

        if requested_zipcode is not None and requested_zipcode[1] == zipcode:
            return ZipcodeResponse(
                zipcode=zipcode,
                risk_factor=requested_zipcode[2],
                exists=True
            )

        return ZipcodeResponse(
            zipcode=zipcode
        )

    """
    # 3.2
    Try to find what's wrong with this implementation and fix it.

    # 3.2.1
    List all the steps that you would take to tackle this bug going from initial discovery to releasing a fix.

    # 3.2.2 How could you easily improve the performance of this route on database level?

    """
    """
    Steps to imporove function:
        1. Use async function
        2. Set a response_model
        3. Add db dependency injector as parameter
        4. Use database package to do async query
        5. Retrun must be the one set in response_model
    """
    @router.get("/databases/zipcodes", response_model=dict)
    async def get_zipcode_by_risk_factor(request: Request, risk_factor: str = Query(None), db: Database = Depends(get_db)) -> dict:
        query = "SELECT zipcode FROM zipcodes WHERE risk_factor = :risk_factor"
        select_zipcode_task = asyncio.create_task(db.fetch_all(query=query, values={"risk_factor": risk_factor}))  # nopep8
        requested_zipcodes = await select_zipcode_task

        if requested_zipcodes is None:
            return {}

        zipcodes = []
        for zipcode in requested_zipcodes:
            zipcodes.append(zipcode[0])

        return {risk_factor: zipcodes}

    return router
