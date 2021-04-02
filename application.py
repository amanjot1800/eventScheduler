from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
import controller as con
from event import Event

app = Flask(__name__)
db = MongoEngine()
print("connecting to database...")
app.config['MONGODB_SETTINGS'] = {
    'db': 'events',
    'host': 'mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler'
}
db.init_app(app)
sub_event = "no sub events"


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':

        if request.form.get("sub_exists") == "yes":
            form = request.form
            con.create_event(form.get('name'),
                             form.get('date'),
                             form.get('time'),
                             form.get('length'),
                             form.get('location'),
                             form.get('guests'),
                             [con.create_sub_event(form.get("sub_name"),
                                                   form.get("sub_date"),
                                                   form.get("sub_time"),
                                                   form.get("sub_length"),
                                                   form.get("sub_location"),
                                                   form.get("sub_guests"))])

        else:
            form = request.form
            con.create_event(form.get('name'),
                             form.get('date'),
                             form.get('time'),
                             form.get('length'),
                             form.get('location'),
                             form.get('guests'),
                             None)
        return redirect(url_for('show_events'))


@app.route('/')
@app.route('/events')
def show_events():
    return render_template('events.html', events=Event.objects)


if __name__ == "__main__":
    app.run(debug=True)
