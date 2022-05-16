import psycopg2
from fastapi import APIRouter, Query
from fastapi.requests import Request


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

    @router.get("/zipcodes/{zipcode}")
    async def get_zipcode_risk_factor(request: Request, zipcode: int):
        # Add your solution here
        pass

    """
    # 3.1
    Retrieve the risk factor for a zipcode from the database.
    The route should return the risk factor for a given zipcode.
    """

    @router.get("/databases/zipcodes/{zipcode}")
    async def get_zipcode_risk_factor_from_database(request: Request, zipcode: int):
        # Add your solution here
        pass

    """
    # 3.2
    Try to find what's wrong with this implementation and fix it.

    # 3.2.1
    List all the steps that you would take to tackle this bug going from initial discovery to releasing a fix.

    # 3.2.2 How could you easily improve the performance of this route on database level?

    """

    @router.get("/databases/zipcodes")
    def get_zipcode_by_risk_factor(request: Request, risk_factor: str = Query(None)):
        # This connection is used only for illustration purposes. Do not use it anywhere else!
        connection = psycopg2.connect(request.app.config.DB_DSN.get_secret_value())
        connection.set_session(autocommit=True)
        zipcodes = []
        with connection.cursor() as cursor:
            cursor.execute(" SELECT zipcode, risk_factor FROM zipcodes WHERE risk_factor = '%s'" % risk_factor)
            results = cursor.fetchall()
            for r in results:
                zipcodes.append(r[0])
        return zipcodes

    return router
