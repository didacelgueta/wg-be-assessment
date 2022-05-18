import logging
from abc import ABC, abstractmethod

from databases import Database
from pydantic import SecretStr

from wg_be_exam.config import Config
from wg_be_exam.db.seeders import ZipcodeSeeder


class AbstractDB(ABC):
    @abstractmethod
    async def setup(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def teardown(self) -> None:
        raise NotImplementedError()


class DB(AbstractDB):
    def __init__(self, dsn: SecretStr):
        self.dsn = dsn
        self.connected = False

    @property
    def connection(self):
        return self.db

    async def setup(self, config: Config) -> None:
        try:
            self.db = Database(self.dsn.get_secret_value())
            await self.db.connect()
            if config.RUN_SEEDER:
                # {'zipcode': 1234, 'risk_factor': 'A'}
                await ZipcodeSeeder(self.db).insert()
                logging.debug(f"DB@setup Zipcode seeder executed")

            self.connected = True
        except Exception as e:
            logging.error(f"Failed to connect to database, got {e}")

    async def teardown(self) -> None:
        if self.connected:
            await self.db.disconnect()
