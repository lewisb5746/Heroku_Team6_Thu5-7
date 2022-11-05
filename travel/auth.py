from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask import g

from . import db

# a blueprint to manage authentication
bp = Blueprint('auth',__name__)




@bp.route('/register', methods = ['GET', 'POST'])  
def register():  
  #create the form
    form = RegisterForm()
    #this line is called when the form - POST
    if form.validate_on_submit():
      print('Register form submitted')
       
      #get username, password and email from the form
      fname = form.first_name.data
      lname = form.last_name.data
      phone = form.phone_num.data
      emailin = form.email.data
      pwd = form.password.data

          

    #   uname =form.username.data
    #   pwd = form.password.data
    #   email=form.email.data
    #   utype =form.usertype.data
      
      pwd_hash = generate_password_hash(pwd)
      #create a new user model object
      new_user = User(first_name=fname, last_name=lname, phone_num=phone, email=emailin, password_hash=pwd_hash)
      db.session.add(new_user)
      db.session.commit()
      flash("Registered user successfully")
      return redirect(url_for('auth.register'))
       
    return render_template('user.html', form=form, heading='Register', user=current_user)
    


@bp.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  error=None
  if(form.validate_on_submit()):
    uemail = form.user_email.data
    password = form.password.data
    u1 = User.query.filter_by(email=uemail).first()
    
        #if there is no user with that name
    if u1 is None:
      error='Incorrect user email'
    #check the password - notice password hash function
    elif not check_password_hash(u1.password_hash, password): # takes the hash and password
      error='Incorrect password'
    if error is None:
    #all good, set the login_user
      login_user(u1)
      print("loged in")
      return redirect(url_for('main.index'))
    else:
      print(error)
      flash(error)
    #it comes here when it is a get method
  return render_template("user.html", form=form, heading='Login', user=current_user)


@bp.route('/logout')
def logout():
  logout_user()
  
  return redirect(url_for("auth.login")), 'Successfully logged out user' 



