from app import create_app


app = create_app()


@app.get("/")
def root():
    return {"message": "Hello from FastAPI with MySQL"}
