import mongoengine as db
from sub_event import SubEvent


class Event(db.Document):
    event_id = db.ObjectIdField()
    name = db.StringField(required=True)
    event_date = db.StringField(required=True)
    event_time = db.StringField(required=True)
    length = db.StringField()
    location = db.StringField()
    guests = db.ListField()
    sub_events = db.EmbeddedDocumentListField(SubEvent)

