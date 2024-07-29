import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from .routes import setup_routes

# Init lifespan of FastAPI application
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup routes
    setup_routes(app, templates)
    yield
    # Close things here

# Load environment variables
load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(lifespan=lifespan)
# Mount the 'static' directory
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
# Setup Jinja2 templates to use the 'templates' directory
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
