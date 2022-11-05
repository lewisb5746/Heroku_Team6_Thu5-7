from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from . import error_handels


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
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    @app.route('/messages/<int:idx>')
    def message(idx):
        messages = ['Message Zero', 'Message One', 'Message Two']
        try:
            return render_template('message.html', message=messages[idx])
        except IndexError:
            abort(404)

    @app.route('/500')
    def error500():
        abort(500)
    
    return app