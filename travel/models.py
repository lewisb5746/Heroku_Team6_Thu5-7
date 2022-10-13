from . import db
from datetime import datetime
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    UserID = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    Last_name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    Phone_num = db.Column(db.int(10), nullabel=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


    comments = db.relationship('Comment', backref='user')
    events_com = db.relationship('Event', secondary='comment', backref=db.backref('commented_users'))
    Ticket_Sold = db.relationship('sale', backref='UserID')

class Artist(db.Model):
    __tablename__ = 'Artist'
    ArtistID = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(30), index=True, unique=True, nullable=False)
    genre = db.Column(db.string(15), nullable=True)
    description = db.column(db.text, nullable=True)
    ImgLinkAristProfile = db.column(db.string(100), nullable=True)

    Event_artist = db.relationship('Event', backref='Event_Artist')

class Event(db.Model):
    __tablename__ = 'Event'
    EnentID = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(30), index=True, unique=True, nullable=False)
    EventDateTime = db.column(db.datetime, nullable=False)
    #genre = db.Column(db.string(15), nullable=True)
    description = db.column(db.text, nullable=True)
    ArtistID = db.column(db.int(10), db.foreignKey('Artist.ArtistID'))
    NumTickets = db.column(db.int(4))
    NumTicketsSold = db.column(db.int(4))
    ImgLink1 = db.column(db.string(100), nullable=True)
    ImgLink2 = db.column(db.string(100), nullable=True)
    ImgLink3 = db.column(db.string(100), nullable=True)

    Ticket_Sold = db.relationship('sale', backref='EventID')
    Type = db.relationship('Ticket_type', backref='EventID')

class Genre(db.model):
    __tablename__ = 'Genre'
    EnentID = db.Column(db.Integer, primary_key=True)
    Genre = db.column(db.string(20), nullable=False)

class Sale(db.Model):
    __tablename__ = 'Sale'
    SaleID = db.Column(db.Integer, primary_key=True)
    EventID = db.Column(db.Int(10), db.ForeignKey('event.EnentID'), nullable=False )
    UserID = db.Column(db.Int(10), db.ForeignKey('user.UserID'), Nullable=False )
    Processing = db.column(db.string(20), nullable=False)
    TicketID = db.column(db.int(6), nullable=False)
    SaleDateTime  =db.column(db.datetime, nullable=False, default=datetime.now())


class Ticket_type(db.model):
    __tablename__ = 'Ticket_type'
    TicketID = db.Column(db.Integer, primary_key=True)
    EnentID = db.Column(db.Integer, db.foreignKey('event.EventID'), nullable=False)
    TikcetName = db.column(db.string(25), nullable=False)
    TikcetDescription = db.column(db.string(100), nullable=True)
    TicketPrice = db.column(db.numeric(15),nullable=False)

class comment(db.Model):
    __tablename__ = 'Comment'
    EventID = db.Column(db.Integer, db.ForeignKey('event.EventID'))
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    CommentID = db.Column(db.Integer, primary_key=True)
    CommentDate = db.column(db.datetime, nullable=False, default=datetime.now())
    Comment = db.column(db.text, nullable=False)










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
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))


#     def __repr__(self):
#         return "<Comment: {}>".format(self.text)

