from event import Event
from sub_event import SubEvent
import mongoengine as db
import controller


def mongo_setup():
    print("connecting...")
    uri = "mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler"
    db.connect(host=uri)


def start():
    controller.create_event("Embeded event", "2020-12-17", "21:00", 2, "Dreams", "Singh, Dabb, Amanjot", None)


mongo_setup()
start()