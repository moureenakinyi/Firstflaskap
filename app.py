from flask import Flask, render_template
from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('about.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=4,max=50)])
    usename = StringField('Username', [validators.length(min=4,max=25)])
    password = PasswordField(),
    validators.DataRequired(),
    validators.EqualTo('confirm', message='Passwords do not match')
    
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
         return render_template('register.html')
    return render_template('register.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)