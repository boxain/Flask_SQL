from .models import db , Users , Comments 
from ..forms import *


def create_table():
    db.create_all()
    

def reset_table():
    db.drop_all()
    db.create_all()


def add_new_user(username , password , email , is_admin=False):
    user = Users(name=username,pwd=password,email=email,is_admin=is_admin)
    try : 
        db.session.add(user)
        db.session.commit()
        return True
    except ValueError as e:
        print("錯誤 : ",e)
        return False











