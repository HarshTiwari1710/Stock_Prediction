from flask import Flask, render_template, request , redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'DpntTellAnyone'
db = SQLAlchemy(app)


class Signup(db.Model):
    email = db.Column(db.String(50), primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(12), unique=True, nullable=False)
class Login(db.Model):
    email = db.Column(db.String(50), primary_key=True, nullable=False)
    password = db.Column(db.String(12), unique=True, nullable=False)
class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])

    submit=SubmitField('Sign up')
class LoginF(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])        

    submit=SubmitField('Login')

@app.route("/")
def hello():
    return render_template('Frontend.html')


@app.route("/Login_&_Signup.html", methods=['GET', 'POST'])
def signup():
    form=LoginForm()
    if request.method=='POST':
        name = form.username.data
        email=form.email.data
        password = form.password.data
        print(name,email,password)
        entry = Signup(name=name,email=email,password=password)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('Desc'))
    return render_template('Login_&_Signup.html',form=form)


@app.route("/Login.html", methods=['GET', 'POST'])
def login():
    form=LoginF()
    if request.method=='POST':
        email=form.email.data
        password = form.password.data
        entry = Login(email=email,password=password)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('Desc'))
    return render_template("Login.html",form=form)


@app.route('/Description.html')
def Desc():
    return render_template('Description.html')
@app.route('/Microsoft.html')
def Microsoft():
    return render_template('Microsoft.html')
@app.route('/Apple.html')
def Apple():
    return render_template('Apple.html')
@app.route('/Mcdonalds.html')
def Mcdonalds():
    return render_template('Mcdonalds.html')
@app.route('/Intel.html')
def Intel():
    return render_template('Intel.html')
@app.route('/Disney.html')
def Disney():
    return render_template('Disney.html')
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8000, debug=True)
