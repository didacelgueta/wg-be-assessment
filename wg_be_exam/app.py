import asyncio
import logging

from fastapi import FastAPI, Request, Response
from databases import Database
from fastapi_redis_cache import FastApiRedisCache

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
        redis_cache = FastApiRedisCache()
        redis_cache.init(
            host_url=app.config.REDIS_URL,
            prefix="myapi-cache",
            response_header="X-MyAPI-Cache",
            ignore_arg_types=[Request, Response, Database]
        )

    @app.on_event("shutdown")
    async def teardown() -> None:
        logging.info(f"[APP_TEARDOWN] {app}")
        await app.state.db.teardown()

    return app


app = create_app(Config())
