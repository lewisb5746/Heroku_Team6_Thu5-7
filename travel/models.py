from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__='User' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), index=True, nullable=False)
    last_name = db.Column(db.String(100), index=True, nullable=False)
    phone_num = db.Column(db.Numeric(10), nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


    comments = db.relationship('Comment', backref='user')
    events_com = db.relationship('Event', secondary='Comment', backref=db.backref('commented_users'))
    tickets_sold = db.relationship('Sale', backref='UserID')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Artist(db.Model):
    __tablename__ = 'Artist'
    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True, nullable=False)
    genre = db.Column(db.String(15), nullable=True)
    description = db.Column(db.String, nullable=True)
    img_link_artist_profile = db.Column(db.String(100), nullable=True)

    event_artist = db.relationship('Event', backref='Event_Artist')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True, nullable=False)
    event_date_time = db.Column(db.DateTime, nullable=False)
    #genre = db.Column(db.string(15), nullable=True)
    description = db.Column(db.String, nullable=True)
    artist_id = db.Column(db.Numeric(10), db.ForeignKey('Artist.artist_id'))
    num_tickets = db.Column(db.Numeric(4))
    num_tickets_sold = db.Column(db.Numeric(4))
    img_link1 = db.Column(db.String(100), nullable=True)
    img_link2 = db.Column(db.String(100), nullable=True)
    img_link3 = db.Column(db.String(100), nullable=True)

    tickets_sold = db.relationship('Sale', backref='EventID')
    type = db.relationship('Ticket_type', backref='EventID')
    comments = db.relationship('Comment', backref='event')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Genre(db.Model):
    __tablename__ = 'Genre'
    event_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(20), nullable=False)

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Sale(db.Model):
    __tablename__ = 'Sale'
    sale_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Numeric(10), db.ForeignKey('Event.event_id'), nullable=False )
    id = db.Column(db.Numeric(10), db.ForeignKey('User.id'), nullable=False )
    processing = db.Column(db.String(20), nullable=False)
    ticket_id = db.Column(db.Numeric(6), nullable=False)
    sale_date_time  =db.Column(db.Time, nullable=False, default=datetime.now())

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)


class Ticket_type(db.Model):
    __tablename__ = 'Ticket_type'
    ticket_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.event_id'), nullable=False)
    ticket_name = db.Column(db.String(25), nullable=False)
    ticket_description = db.Column(db.String(100), nullable=True)
    ticket_price = db.Column(db.Numeric(15),nullable=False)

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'Comment'
    comment_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.event_id'))
    id = db.Column(db.Integer, db.ForeignKey('User.id'))
    comment_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    comment_text = db.Column(db.String, nullable=False)

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)










# #dont use bellow
# class Destination(db.Model):
#     __tablename__ = 'destinations'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     description = db.Column(db.String(200))
#     image = db.Column(db.String(400))
#     currency = db.Column(db.String(3))
#     # ... Create the Comments db.relationship
# 	# relation to call destination.comments and comment.destination
#     comments = db.relationship('Comment', backref='destination')

    
	
#     def __repr__(self): #string print method
#         return "<Name: {}>".format(self.name)

# class Comment11(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(400))
#     created_at = db.Column(db.DateTime, default=datetime.now())
#     #add the foreign keys
#     id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))


#     def __repr__(self):
#         return "<Comment: {}>".format(self.text)

