from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
db = PyMongo(app,
             uri='mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler?retryWrites=true&w=majority').db


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/insert', methods=['POST'])
def insert():
    form = request.form
    db.events.insert_one(
        {'name': form.get('name'), 'time': form.get('time'), 'location': form.get('location'),
         'length': form.get('length')})
    return 'added'


@app.route('/events')
def show_events():
    val = []
    for event in db.events.find():
        val.append(event)

