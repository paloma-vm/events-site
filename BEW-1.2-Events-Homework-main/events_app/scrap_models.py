"""Create database models to represent tables."""
from events_app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base


# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table


class Guest(db.Model):
    __tablename__ = 'guest'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    events_attending = db.relationship("Event", secondary='event_guest', back_populates="guests")


    def __str__(self):
        return f'<Guest: {self.name}>'

    def __repr__(self):
        return f'<Guest: {self.name}>'

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(300))
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship("Guest", secondary='event_guest', back_populates="events")

    def __str__(self):
        return f'<Event: {self.title}>'

    def __repr__(self):
        return f'<Eventt: {self.title}>'

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)


# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)

# guest_event_table = None

event_guest_table = Table('event_guest', 
    Column('event_id', db.Integer, ForeignKey('event.id')),
    Column('guest_id', db.Integer, ForeignKey('guest.id'))
)
