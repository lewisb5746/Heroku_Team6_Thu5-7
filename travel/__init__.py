from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.debug=True

    #we use this utility module to display forms quickly
    bootstrap = Bootstrap4(app)

    #A secret key for the session object
    app.secret_key='somerandomvalue'

    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///entertainment_events.sqlite'
    db.init_app(app)

    #login stuff
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .views import mainbp
    app.register_blueprint(mainbp)

    # register the blueprint with the app
    from .auth import bp
    app.register_blueprint(bp)

    #add Blueprints
    # from . import views
    # app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    #from . import auth
    #app.register_blueprint(auth.bp)

    return app