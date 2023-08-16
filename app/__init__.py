from fastapi import FastAPI
from . import routes, models
from .database import engine


def create_app():
    models.Base.metadata.create_all(bind=engine)

    app = FastAPI()
    routes.browser_router(app)
    return app
