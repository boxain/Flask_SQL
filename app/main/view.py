from . import main_bp



@main_bp.route("/",methods=["GET"]) #首頁
def main_page():
    pass



@main_bp.route("/register",methods=["GET","POST"]) #註冊
def register_page():
    pass



@main_bp.route("/login",methods=["GET","POST"]) #登入
def login_page():
    pass



@main_bp.route("/forgot_password",methods=["GET","POST"]) #忘記密碼
def forgot_password_page():
    pass



