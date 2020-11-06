from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, EqualTo, Email, NumberRange, InputRequired
from wtforms.validators import Regexp, URL, ValidationError


# 表單驗証
class RegisterForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message='用戶名長度不正確')])
    password = StringField(validators=[Length(min=3, max=10, message='密碼長度不正確')])
    password_verify = StringField(validators=[EqualTo('password', message='兩次密碼不一致')])


class LoginForm(Form):
    # email = StringField(validators=[Email(message="格式不正確")])
    # NumberRange
    # age = IntegerField(validators=[NumberRange(min=1, max=80, message="年齡不正確")])
    # InputRequired
    # username = StringField(validators=[InputRequired(message="必須輸入")])
    # phone = StringField(validators=[Regexp(r'1[3589]\d{9}')])
    # url_info = StringField(validators=[URL()])
    # 驗証碼
    captcha = StringField(validators=[Length(min=4, max=4)])

    # 類名固定 開頭 ︰ vaildate_ , 驗証參數 ︰ captcha
    def vaildate_captcha(self, field):
        if field.data != '5678':
            raise ValidationError('驗証碼錯誤')
