from crypt import methods
from . import course_bp


@course_bp.route("/course/base" , methods=["GET","POST"])
def course_base_page():
    pass



@course_bp.route("/course/insert" , methods=["GET","POST"])
def course_insert_page():
    pass



@course_bp.route("/course/delete" , methods=["GET","POST"])
def course_delete_page():
    pass



@course_bp.route("/course/update" , methods=["GET","POST"])
def course_update_page():
    pass



@course_bp.route("/course/select" , methods=["GET","POST"])
def course_select_page():
    pass



@course_bp.route("/course/advanced" , methods=["GET","POST"])
def course_advanced_page():
    pass