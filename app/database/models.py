from ctypes import c_void_p
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash , check_password_hash
from datetime import datetime


db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50) , nullable=False)
    password = db.Column(db.String(200) , nullable=False)
    email = db.Column(db.String(50) , nullable=False)
    introduction = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean , nullable=False , default=False)
    register_time = db.Column(db.DateTime , default=datetime.now , nullable=False)
    comments = db.relationship("comments")
    records = db.relationship("records")

    def __init__(self,name,password,email) -> None:
        self.name = name
        self.password = generate_password_hash(password)
        self.email = email

    def check_password(self,password):
        return check_password_hash(self.password,password)



class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer , primary_key=True)
    u_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    post_id = db.Column(db.Integer , nullable=False)
    content = db.Column(db.String(50) , nullable=False)
    time = db.Column(db.DateTime , default=datetime.now , nullable=False)
    questions = db.relationship("questions")

    def __init__(self, u_id, post_id, content) -> None:
        self.u_id = u_id
        self.post_id = post_id
        self.content = content
    


class Questions():
    __tablename__ = "questions"
    id = db.Column(db.Integer , primary_key=True)   
    q_name = db.Column(db.String(50) , nullable=False)
    c_id = db.Column(db.Integer , db.ForeignKey("comments.id"),nullable=False)
    is_word = db.Column(db.Boolean , nullable=False , default=False)
    topics = db.relationship("topics")

    def __init__(self,name, c_id, is_word) -> None:
        self.name = name
        self.c_id = c_id
        self.is_word = is_word



class Books():
    __tablename__ = "book"
    id = db.Column(db.Integer , primary_key=True)
    b_name = db.Column(db.String(50) , nullable=False)
    topics = db.relationship("topics")

    def __init__(self,name) -> None:
        self.b_name = name



class Topics():
    __tablename__ = "topics"
    id = db.Column(db.Integer , primary_key=True)
    t_name = db.Column(db.String(50) , nullable=False)
    b_id = db.Column(db.Integer , db.ForeignKey("books.id"),nullable=False)
    q_id = db.Column(db.Integer , db.ForeignKey("questions.id"),nullable=False)
    records = db.relationship("records")

    def __init__(self,name,b_id, q_id) -> None:
        self.t_name = name
        self.b_id = b_id
        self.q_id = q_id



class Records():
    __tablename__ = "records"
    id = db.Column(db.Integer , primary_key=True)
    u_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    t_id = db.Column(db.Integer , db.ForeignKey("topics.id"),nullable=False)

    def __init__(self,u_id, q_id) -> None:
        self.u_id = u_id
        self.q_id = q_id