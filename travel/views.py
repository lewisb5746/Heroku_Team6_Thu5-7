from flask import Blueprint, render_template, request, redirect,url_for
from .models import Event

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = Event.query.all()    
    return render_template('index.html', events=events)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        event = "%" + request.args['search'] + '%'
        events = Event.query.filter(Event.description.like(event)).all()
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))