from flask import Flask, render_template, request
from flask_mongoengine import MongoEngine
import controller as con


app = Flask(__name__)
db = MongoEngine()
app.config['MONGODB_SETTINGS'] = {
    'db': 'event',
    'host': 'mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler'
}
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html')


@app.route('/insert', methods=['POST'])
def insert():
    form = request.form
    con.create_event(form.get('name'), form.get('date'), form.get('time'), form.get('length'),
                     form.get('location'), form.get('guests'))
    return 'added'


@app.route('/events')
def show_events():
    val = []


if __name__ == "__main__":
    app.run(debug=True)
