from locale import currency
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event, Comment, User, Artist
from datetime import datetime
from .forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import current_user


bp = Blueprint('event', __name__, url_prefix='/events')

@bp.route('/<event_id>')
def show(event_id):
    event = Event.query.filter_by(event_id=event_id).first()
    user = User.query.filter_by(id=event.created_by).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('events/show.html', event=event, user=user, form=cform)

@bp.route('/create', methods = ['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():
    #call the function that checks and returns image
    #db_file_path= '/static/image/event.png'
    db_file_path= check_upload_file(form)
    event=Event(name=form.name.data,description=form.description.data, 
    img_link1=db_file_path,num_tickets=form.num_tickets.data,event_date_time=datetime.now(),created_by=current_user.id)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    print('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('event.create'))
  return render_template('events/create.html', form=form)

@bp.route('/update/<event_id>', methods = ['GET', 'POST'])
def update(event_id):
  print('Method type: ', request.method)
  event = Event.query.filter_by(event_id=event_id).first()
  artist = Artist.query.filter_by(artist_id=event.artist_id).first()
  form = EventForm()
  return render_template('events/update.html', event=event, artist_obj=artist, form=form)  

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/image/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<event_id>/comment', methods = ['GET', 'POST'])  
def comment(event_id):  
    form = CommentForm()  
    #get the event object associated to the page and the comment
    event_obj = Event.query.filter_by(event_id=event_id).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(comment_text=form.text.data,  
                        event_id=event_id)
      #here the back-referencing works - comment.event is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to event.show
    return redirect(url_for('event.show', event_id=event_id))
    