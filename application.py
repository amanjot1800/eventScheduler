from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
import controller as con
from event import Event

app = Flask(__name__)
db = MongoEngine()
print("connecting to database...")
app.config['MONGODB_SETTINGS'] = {
    'db': 'event',
    'host': 'mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler'
}
db.init_app(app)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':

        if request.form.get("sub_exists3") == "yes" and request.form.get("sub_exists2") == "yes" and \
                request.form.get("sub_exists1") == "yes":

            form = request.form
            con.create_event(form.get('name'),
                             form.get('date'),
                             form.get('time'),
                             form.get('length'),
                             form.get('location'),
                             form.get('guests'),
                             [con.create_sub_event(form.get("sub_name1"),
                                                   form.get("sub_date1"),
                                                   form.get("sub_time1"),
                                                   form.get("sub_length1"),
                                                   form.get("sub_location1"),
                                                   form.get("sub_guests1")),
                              con.create_sub_event(form.get("sub_name2"),
                                                   form.get("sub_date2"),
                                                   form.get("sub_time2"),
                                                   form.get("sub_length2"),
                                                   form.get("sub_location2"),
                                                   form.get("sub_guests2")),
                              con.create_sub_event(form.get("sub_name3"),
                                                   form.get("sub_date3"),
                                                   form.get("sub_time3"),
                                                   form.get("sub_length3"),
                                                   form.get("sub_location3"),
                                                   form.get("sub_guests3"))])

        elif request.form.get("sub_exists2") == "yes" and request.form.get("sub_exists1") == "yes":
            form = request.form
            con.create_event(form.get('name'),
                             form.get('date'),
                             form.get('time'),
                             form.get('length'),
                             form.get('location'),
                             form.get('guests'),
                             [con.create_sub_event(form.get("sub_name1"),
                                                   form.get("sub_date1"),
                                                   form.get("sub_time1"),
                                                   form.get("sub_length1"),
                                                   form.get("sub_location1"),
                                                   form.get("sub_guests1")),
                              con.create_sub_event(form.get("sub_name2"),
                                                   form.get("sub_date2"),
                                                   form.get("sub_time2"),
                                                   form.get("sub_length2"),
                                                   form.get("sub_location2"),
                                                   form.get("sub_guests2"))])

        elif request.form.get("sub_exists1") == "yes":
            form = request.form
            con.create_event(form.get('name'),
                             form.get('date'),
                             form.get('time'),
                             form.get('length'),
                             form.get('location'),
                             form.get('guests'),
                             [con.create_sub_event(form.get("sub_name1"),
                                                   form.get("sub_date1"),
                                                   form.get("sub_time1"),
                                                   form.get("sub_length1"),
                                                   form.get("sub_location1"),
                                                   form.get("sub_guests1"))])

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


@app.route('/delete/<id>')
def delete(id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect(url_for('show_events'))


if __name__ == "__main__":
    app.run(debug=True)
