from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler"
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/insert', methods=['POST'])
# def insert():
#     form = request.form
#     mongo.db.events.insert_one(
#         {'name': form.get('name'), 'time': form.get('time'), 'location': form.get('location'), 'length': form.get('length')})
#     return 'added'
