from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    """
    displays dashboard/homepage for stock screener
    """
    return {"DashBoard": "FastAPI-World"}


@app.post("/stock")
def create_stock():
    """
    end point to create a stock item and store in database
    """
    return{
        "code": "success",
        "message": "stock created"

    }


