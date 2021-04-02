import mongoengine as db


class SubEvent(db.EmbeddedDocument):
    event_id = db.ObjectIdField()
    name = db.StringField()
    event_date = db.StringField()
    event_time = db.StringField()
    length = db.StringField()
    location = db.StringField()
    guests = db.ListField()
