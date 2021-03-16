import controller

print("Connecting to database...")
controller.mongo_setup()


def start():
    if input("Press 1 to create an event: \n"):
        name = input("Event Title: ")
        time = input("Event Date and Time (format DD MM YYYY HH:MM): ")
        length = input("Event length: ")
        location = input("Event location: ")
        guests = input("Guests (separate by comma and space): ")

        controller.create_event(name, time, length, location, guests)


start()
