from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#Create new destination
class EventForm(FlaskForm):
  name = StringField('EventName', validators=[InputRequired()])
  #eventDateTime = StringField('Event Date Time', validators=[InputRequired()])
  eventDateTime = DateTimeField('Event Date Time (yyyy-mm-dd HH:MM)', validators=[InputRequired()], format='%Y-%m-%d %H:%M')
  description = TextAreaField('Description', validators=[InputRequired()])
  artist = StringField('Artist Name', validators=[InputRequired()])
  num_tickets = IntegerField('Number Of Tickets', validators=[InputRequired()])
  image = FileField('Event Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  submit = SubmitField("Create")
    #test
#User login
class LoginForm(FlaskForm):
    user_email=StringField("Email", validators=[InputRequired('Enter user email')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    fist_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone_num = IntegerField('Phone Number', validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')