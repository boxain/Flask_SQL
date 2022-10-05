from crypt import methods
from . import user_bp


@user_bp.route("/user/data",methods=["GET"])
def user_data_page():
    pass



@user_bp.route("/user/login_days",methods=["GET"])
def user_login_days():
    pass



@user_bp.route("/user/write_questions",methods=["GET"])
def user_write_questions():
    pass



@user_bp.route("/user/collect_questions",methods=["GET"])
def user_collect_questions():
    pass
