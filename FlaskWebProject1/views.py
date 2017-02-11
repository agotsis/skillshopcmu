"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import sqlite3
from flask import g, Flask, jsonify, request

DATABASE = []
class DB ():
  def __init__(this,name,password):
    this.name = name
    this.password = password
    this.skills = [[],[],[]]

# END DB CLASS

@app.route('/field_lookup', methods = ['POST'])
def db_lookup():
  name = request.form.get('id')
  for i in range(len (DATABASE)):
    if (DATABASE[i].name == name):
      return jsonify(DATABASE[i].skills)
  return jsonify(None)

@app.route('/field_set', methods=['POST'])
def db_append():
  id = request.form.get('id')
  password = request.form.get('password')
  p = DB(id, password)
  DATABASE.append(p)
  return jsonify("Success");

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/user_tests')
def user_tests():
    """User unit tests."""
    return render_template(
        'user_index.html',
    )
"""if (__name__ == '__main__'):
  get_db().execute(
CREATE TABLE USERS(
  ID INT PRIMARY KEY NOT NULL,
  ANDREW TEXT NOT NULL,
  PASSWORD TEXT NOT NULL,
  CONVERSATIONAL TEXT,
  PRACTICE TEXT,
  TEACH TEXT
  );)
  app.run()"""
