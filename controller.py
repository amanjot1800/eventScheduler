from event import Event
from sub_event import SubEvent


def create_event(name, date, time, length, location, guests, sub_events):

    event = Event()
    event.name = name
    event.event_date = date
    event.event_time = time
    event.length = length
    event.location = location
    event.guests = guests.split(", ")
    event.sub_events = sub_events
    event.save()


def create_sub_event(name, date, time, length, location, guests):
    event = SubEvent()
    event.name = name
    event.event_date = date
    event.event_time = time
    event.length = length
    event.location = location
    event.guests = guests.split(", ")
    return event
