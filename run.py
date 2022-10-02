from app import create_app
from dotenv import load_dotenv
from os import getenv
from flask_migrate import Migrate
from app.database import db
from app.database.helper import add_new_user , create_table , reset_table




load_dotenv()
app = create_app(getenv("FLASK_ENV"))
Migrate(app,db,render_as_batch=True) # 用sqlite最後一個參數必須設定


@app.cli.command(name="create_table")
def create_all_table():
    create_table()


@app.cli.command(name="reset_table")
def reset_all_table():
    reset_table()


@app.cli.command(name="add_user")
def add_user():
    name = input("Name : ")
    password = input("Password : ")
    email = input("Email : ")
    if add_new_user(name,password,email):
        print("OK !")
    else :
        print("Failed....")


















