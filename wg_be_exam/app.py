import asyncio
import logging

from fastapi import FastAPI

import wg_be_exam.routes as routes
from wg_be_exam.config import Config
from wg_be_exam.db import DB


def create_app(config: Config):
    app = FastAPI(title='WeGroup Assessment', openapi_url="/openapi/spec.json", redoc_url="/redoc")
    app.config = Config()
    app.include_router(routes.get_index_router())
    app.include_router(routes.get_zipcode_router())

    app.state.db = DB(dsn=config.DB_DSN)
    app.repositories = lambda: None

    @app.on_event("startup")
    async def setup() -> None:
        logging.info(f"[APP_SETUP] {app}")
        app.loop = asyncio.get_running_loop()
        await app.state.db.setup(app.config)

    @app.on_event("shutdown")
    async def teardown() -> None:
        logging.info(f"[APP_TEARDOWN] {app}")
        await app.state.db.teardown()

    return app


app = create_app(Config())
