from event import Event


def create_event(name, date, time, length, location, guests):

    event = Event()
    event.name = name
    event.event_date = date
    event.event_time = time
    event.length = int(length)
    event.location = location
    event.guests = guests.split(", ")
    event.save()


def get_events():
    events = Event().objects
    for event in events:
        print(event)
