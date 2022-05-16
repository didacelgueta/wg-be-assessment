from __future__ import absolute_import

from pydantic import BaseSettings, SecretStr

try:  # nosec
    from dotenv import load_dotenv

    load_dotenv(verbose=True)
except Exception:  # nosec
    pass


class Config(BaseSettings):
    DB_DSN: SecretStr
    ENVIRONMENT: str
