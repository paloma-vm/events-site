"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

guest_event_table = Table('association', db.metadata, 
    Column('left_id', ForeignKey('left.id'), primary_key=True),
    Column('right_id', ForeignKey('right.id'), primary_key=True)
)

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table


class Guest(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    events_attending = db.relationship("Event", secondary=guest_event_table)

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

class Event(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship("Guest", secondary=guest_event_table, back_populates="events")

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)


# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)

# guest_event_table = None

# guest_event_table = Table('association', db.metadata, 
#     Column('event_id', ForeignKey('event.id')),
#     Column('guest_id', ForeignKey('guest.id'))
# )
