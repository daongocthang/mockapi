from fastapi import FastAPI, APIRouter, Depends
from app import crud, schemas
from ..database import get_db
from sqlalchemy.orm import Session


def browser_router(app: FastAPI):
    import os
    import pkgutil
    import sys

    cend = "\33[0m"
    cred = "\33[31m"
    base_dir = os.path.dirname(__file__)
    sys.path.append(base_dir)
    try:
        for _, modname, _ in pkgutil.iter_modules([base_dir]):
            mod = __import__(modname)
            app.include_router(mod.router)
    except AttributeError as e:
        print(
            f"{cred}ERROR{cend}:",
            " " * 2,
            f"Module '{cred}{modname}{cend}' has no attribute 'routes'. Initialize router failed.",
        )
