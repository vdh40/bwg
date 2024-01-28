from fastapi import FastAPI

from bwg_app.controllers.fastapi.router import router
from bwg_app.core.config import config


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url="{}/docs".format(config.api_prefix),
        openapi_url="{}/openapi.json".format(config.api_prefix)
    )

    setup_routers(app)

    return app


def setup_routers(app: FastAPI):
    app.include_router(router, prefix=config.api_prefix)
