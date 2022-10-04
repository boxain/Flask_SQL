from flask import Blueprint

main_bp = Blueprint("main",__name__) # __name__ == 路徑名稱
from . import view