import logging
from abc import ABC, abstractmethod

from databases import Database
from pydantic import SecretStr


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

    async def setup(self) -> None:
        try:
            self.db = Database(self.dsn.get_secret_value())
            await self.db.connect()
            await self.db.execute("SELECT now();")  # Test connection
            self.connected = True
        except Exception as e:
            logging.error(f"Failed to connect to database, got {e}")

    async def teardown(self) -> None:
        if self.connected:
            await self.db.disconnect()
