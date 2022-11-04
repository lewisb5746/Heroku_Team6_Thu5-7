from flask import Blueprint, render_template, request, redirect,url_for
from flask_login import login_required, current_user

from .models import Event, User

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = Event.query.all()
    user = User.query.first()f
    return render_template('index.html', events=events, user=current_user)

@mainbp.route('/update/<user_id>', methods = ['GET', 'POST'])
def update(user_id):
  print('Method type: ', request.method)
  user = User.query.filter_by(id=user_id).first()
  events = Event.query.filter_by(created_by=user_id).all()
  return render_template('events/my_events.html', user=current_user, events=events)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        ev = "%" + request.args['search'] + '%'
        events = Event.query.filter(Event.description.like(ev)).all()
        return render_template('index.html', events=events, user=current_user)
    else:
        return redirect(url_for('main.index', user=current_user))