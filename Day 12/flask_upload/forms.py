from wtforms import Form, StringField, IntegerField, FileField
from wtforms.validators import Length, EqualTo, InputRequired
from flask_wtf.file import FileRequired, FileAllowed


class UploadForm(Form):
    image_file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    desc = StringField(validators=[InputRequired()])
