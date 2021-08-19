from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import IntegerField
from wtforms.validators import DataRequired, EqualTo
from models import *

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('repassword')])
    # EqualTo는 비밀번호 확인과 같은지 검사한다.
    repassword = PasswordField('repassword', validators=[DataRequired()])

class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self,message=None):
            self.message = message

        def __call__(self, form, field):
            userid = form['userid'].data
            password = form['password'].data
            usertable = db_session.query(User).filter(User.userid==userid).first()
            check_userid = usertable.userid
            check_pw = usertable.password

            if check_userid != userid:
                raise ValueError('아이디 틀림')
            if check_pw != password:
                raise ValueError('비밀번호가 틀렸습니다')

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])

class Admin_RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('repassword')])
    # EqualTo는 비밀번호 확인과 같은지 검사한다.
    repassword = PasswordField('repassword', validators=[DataRequired()])
    point = IntegerField('point', validators=[DataRequired()])
