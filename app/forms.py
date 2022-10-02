from cProfile import label
from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField , SubmitField , PasswordField , EmailField , TextAreaField
from wtforms.validators import DataRequired , Length , EqualTo , Regexp , Optional


class LoginForm(FlaskForm):
    username = StringField(
        lable = "Username",
        validators=[
            DataRequired(),
        ],
        render_kw={"placeholder":"Username","class":"LoginForm"}
    )

    password = PasswordField(
        label = "Password",
        validators = [
            DataRequired()
        ],
        render_kw={"placeholder":"Password","class":"LoginForm"}    
    )

    submit = SubmitField(
        label="Login"
    )



class RegisterForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[
            DataRequired(),
            Length(min=4,max=20,message="The name should be 4 to 20 letters"),
            Regexp("[a-zA-Z0-9_]+",message="Only letters, numbers and underscores are allowed in username")
        ],
        render_kw={"placeholder":"Username","class":"RegisterForm"}
    )

    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=6,max=15,message="The password must contain at least 6 letters")            
        ],
        render_kw={"placeholder":"Password","class":"RegisterForm"}
    )

    repeat_password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            # 比對欄位要是字串
            EqualTo("password",message="Password not match")          
        ],
        render_kw={"placeholder":"Repeat_Password","class":"RegisterForm"}
    )

    email = EmailField(
        label="Email",
        validators=[DataRequired()],
        render_kw={"placeholder":"Email","class":"RegisterForm"}
    )

    submit = SubmitField(
        label="Register",
    )



class CommentForm(FlaskForm):
    add_comment = StringField(
        label="content-comment",
        validators=[DataRequired()],
        render_kw={"placeholder":"Content","class":"CommentForm"}
    )

    submit = SubmitField("Add !")



class ForgotForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[
            DataRequired(),
            Length(min=4,max=20,message="The name should be 4 to 20 letters"),
            Regexp("[a-zA-Z0-9_]+",message="Only letters, numbers and underscores are allowed in username")
        ],
        render_kw={"placeholder":"Username","class":"ForgotForm"}
    )
    
    new_password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=6,max=15,message="The password must contain at least 6 letters")            
        ],
        render_kw={"placeholder":"New_Password","class":"ForgotForm"}
    )

    repeat_password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            # 比對欄位要是字串
            EqualTo("new_password",message="Password not match")          
        ],
        render_kw={"placeholder":"Repeat_Password","class":"ForgotForm"}
    )

    submit = SubmitField(
        label="Setting",
    )



class SQL_exe(FlaskForm):
    query = TextAreaField(label="Query")
    commit = SubmitField(label="commit")
    