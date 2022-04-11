from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import SubmitField, FileField
from flask import render_template, redirect, url_for, flash, request
from flask import Blueprint
import algorithm
bp = Blueprint('index', __name__)

class ImageForm(FlaskForm):
    image = FileField(u'', validators=[FileAllowed(['jpg'])])
    submit = SubmitField('Recognize!')

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    if form.validate_on_submit():
        file = request.files['image']
        tmp_filepath = f"./tmp/garbage.jpg"
        file.save(tmp_filepath)
        result = algorithm.run(tmp_filepath, './model01.pt', './Garbage classification')
        return render_template('result.html', title='Recognition result', result=result)
    return render_template('index.html', title='Recognize garbage', form=form)

@bp.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html', title='Recognition result')

