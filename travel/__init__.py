from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    #we use this utility module to display forms quickly
    bootstrap = Bootstrap(app)

    #A secret key for the session object
    app.secret_key='somerandomvalue'

    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///entertainment_events.sqlite'
    db.init_app(app)

    #login stuff
    login_manager = LoginManager()
    login_manager.login_view=""

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app