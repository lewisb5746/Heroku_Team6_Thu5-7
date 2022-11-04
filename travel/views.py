from flask import Blueprint, render_template, request, redirect,url_for
from .models import Event
from flask_login import login_required, current_user


mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = Event.query.all()    
    return render_template('index.html', events=events, user=current_user)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        ev = "%" + request.args['search'] + '%'
        events = Event.query.filter(Event.description.like(ev)).all()
        return render_template('index.html', events=events, user=current_user)
    else:
        return redirect(url_for('main.index', user=current_user))