import mongoengine as db
from event import Event


def mongo_setup():
    CON_URI = "mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler"
    db.connect(host=CON_URI)


def create_event(name, time, length, location, guests):

    event = Event()
    event.name = name
    event.event_date
    event.event_time = time
    event.length = int(length)
    event.location = location
    event.guests = guests.split(", ")
    event.save()
