from databases import Database
import asyncio


class InsertValue:
    @staticmethod
    async def handle(zipcode: int, risk_factor: str, db: Database) -> None:
        task_select_data = asyncio.create_task(db.execute(
            f"SELECT count(*) FROM zipcodes WHERE zipcode = {zipcode} AND risk_factor = '{risk_factor}';"))
        data_found = await task_select_data

        if data_found == 0:
            query = "INSERT INTO zipcodes(zipcode, risk_factor) VALUES (:zipcode, :risk_factor)"
            values = {'zipcode': zipcode, 'risk_factor': risk_factor}
            await db.execute(query=query, values=values)
