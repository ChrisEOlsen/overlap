import os
from dotenv import load_dotenv
from fastapi import Request, FastAPI, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates

def setup_routes(app: FastAPI, templates: Jinja2Templates):
    @app.get("/", response_class=HTMLResponse)
    async def read_root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})


    print("setup_routes called")
