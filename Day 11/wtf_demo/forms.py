from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo


# 表單驗証
class RegisterForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message='用戶名長度不正確')])
    password = StringField(validators=[Length(min=3, max=10, message='密碼長度不正確')])
    password_verify = StringField(validators=[EqualTo('password', message='兩次密碼不一致')])
