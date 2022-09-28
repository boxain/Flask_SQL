from turtle import hideturtle
from venv import create

from app import create_app
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app = create_app(getenv("FLASK_ENV"))

