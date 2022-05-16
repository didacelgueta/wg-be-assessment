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
    RUN_SEEDER = True
    URL_HEALT_INDEXES = 'https://bestat.statbel.fgov.be/bestat/api/views/48744f07-252a-4a42-bca3-a2d7cb31c2fd/result/EMBEDDED_HTML'
