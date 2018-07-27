import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  sensor = db.Column(db.String(40));
  record_datetime = db.Column(db.DateTime);
  value = db.Column(db.Float);

  def __init__(self, sensor, record_datetime, value):
    self.sensor = sensor;
    self.record_datetime = record_datetime;
    self.value = value;


@app.route('/sensors_values', methods=['GET'])
def index():
  return "HOLA"; #render_template('index.html', users=User.query.all())


@app.route('/sensors_values', methods=['POST'])
def user():
  u = User(request.form['sensor'], request.form['record_datetime'],request.form['value'])
  db.session.add(u)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  db.create_all()
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
