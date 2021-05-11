from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'DontTellAnyone'


class LoginForm(Form):
    username = StringField('username',
                           validators=[InputRequired(), Email(message='Please enter a valid email address')])
    username.label = 'User Name'
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=5, max=10), AnyOf('secret', 'password')])
    password.label = 'Password'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Form successfully submitted!'

    return render_template('index.html', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)
