import mongoengine as db
import datetime


class Event(db.Document):

    event_id = db.ObjectIdField()
    name = db.StringField(required=True)
    event_time = db.StringField()
    length = db.FloatField(required=True)
    location = db.StringField()
    guests = db.ListField()


    # def __init__(self, *args, **values):
    #
    #     super().__init__(*args, **values)
    #     self.event_id = db.ObjectIdField()
    #     self.name = db.StringField(required=True)
    #     self.event_time = db.DateTimeField(default=datetime.datetime.now)
    #     self.length = db.FloatField(required=True)
    #     self.location = db.StringField
    #     self.guests = db.ListField
    #
    # @property
    # def event_id(self):
    #     return self.event_id
    #
    # @event_id.setter
    # def event_id(self, value):
    #     self._event_id = value
    #
    # @property
    # def name(self):
    #     return self.name
    #
    # @property
    # def event_time(self):
    #     return self.event_time
    #
    # @property
    # def length(self):
    #     return self.length
    #
    # @property
    # def location(self):
    #     return self.location
    #
    # @property
    # def guests(self):
    #     return self.guests
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value
    #
    # @event_time.setter
    # def event_time(self, value):
    #     self._event_time = value
    #
    # @length.setter
    # def length(self, value):
    #     self._length = value
    #
    # @location.setter
    # def location(self, value):
    #     self._location = value
    #
    # @guests.setter
    # def guests(self, value):
    #     self._guests = value
