from abc import ABC, abstractmethod
from typing import Optional
from databases import Database
import asyncio

from wg_be_exam.actions.readZipcodesFile import ReadZipcodesFile
from wg_be_exam.actions.insertValue import InsertValue


class AbstractSeeder(ABC):
    def __init__(self, db: Database) -> None:
        self.db = db

    @abstractmethod
    async def insert(self, data: Optional[dict] = None) -> None:
        raise NotImplementedError


class ZipcodeSeeder(AbstractSeeder):
    async def insert(self, data: Optional[dict] = None) -> None:
        if data is not None:
            await InsertValue.handle(data['zipcode'], data['risk_factor'], self.db)

            return None

        df_zipcodes = ReadZipcodesFile.handle('zipcodes.csv')

        for zipcode, risk_factor in df_zipcodes.iterrows():
            await InsertValue.handle(zipcode, risk_factor.values[0], self.db)
