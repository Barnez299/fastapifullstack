# from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# define templates directory

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    """
    displays dashboard/homepage for stock screener
    """
    return templates.TemplateResponse("home.html",{
        "request": request
    })


@app.post("/stock")
def create_stock():
    """
    end point to create a stock item and store in database
    """
    return{
        "code": "success",
        "message": "stock created"

    }


