from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange, ValidationError
from flask_wtf.file import FileRequired, FileField, FileAllowed
from .models import User


ALLOWED_FILE = {'PNG','JPG','png','jpg'}

def VaildEmail(self, field):
      user = User.query.filter_by(email=field.data).first()
      if user:
        raise ValidationError("An Account under this email has already been used")

#Create new destination
class EventForm(FlaskForm):
  name = StringField('', validators=[InputRequired()])
  #eventDateTime = StringField('Event Date Time', validators=[InputRequired()])
  eventDateTime = DateTimeField('', validators=[InputRequired()], format='%Y-%m-%d %H:%M:%S')
  description = TextAreaField('', validators=[InputRequired()])
  artist = StringField('', validators=[InputRequired()])
  num_tickets = IntegerField('', validators=[InputRequired()])
  image = FileField('', validators=[
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
    
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone_num = IntegerField('Phone Number', validators=[InputRequired(),NumberRange(min=9999999,max=1000000000000,message='Enter a phone number 8 to 12 didgets long') ])
    email = StringField("Email Address", validators=[Email("Please enter a valid email"),VaildEmail])
    
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

