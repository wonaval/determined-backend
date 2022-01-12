import os
import datetime
from flask import Flask, request
from flask_cors import CORS
import sqlalchemy
app = Flask(__name__)
CORS(app)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import jwt

from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
import models
models.db.init_app(app)

# --- USER ROUTES ---
# Create user - POST - /user - Tested? OK
def create_user():
  hashed_pw = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
  # try:
  user = models.User(
    name=request.json['name'],
    username=request.json['username'],
    email=request.json['email'],
    password=hashed_pw
  )
  models.db.session.add(user)
  models.db.session.commit()
  encrypted_id = jwt.encode({'user_id' : user.id}, os.environ.get('JWT_SECRET'), algorithm='HS256')
  return {
    'user' : user.to_json(),
    'user_id' : encrypted_id
  }
  # except:
  #   return { 'message' : 'Email must be present and unique' }, 400
app.route('/user', methods=['POST'])(create_user)

# Verify user - GET - /user/verify - Tested? OK
def verify_user():
  decypted_id = jwt.decode(request.headers['Authorization'], os.environ.get('JWT_SECRET'), algorithms=['HS256'])['user_id']
  user = models.User.query.filter_by(id=decypted_id).first()
  if user:
    return {'user' : user.to_json()}
  else:
    return {'message' : 'User not found'}
app.route('/user/verify', methods=['GET'])(verify_user)

# Login user - POST - /user/login - Tested? OK
def login():
    user = models.User.query.filter_by(email=request.json['email']).first()
    if not user:
      return { 'message' : 'User not found'}, 404
    if bcrypt.check_password_hash(user.password, request.json['password']):
      encrypted_id = jwt.encode({'user_id' : user.id}, os.environ.get('JWT_SECRET'), algorithm='HS256')
      return { 
        "user" : user.to_json(),
        'user_id' : encrypted_id
        }
    else:
      return { 'message' : 'Login failed'}, 401
app.route('/user/login', methods=['POST'])(login)

# Update user - PUT - /user/:user_id - Tested? OK
# Delete user - DELETE - /user/:user_id - Tested? OK
def user_func():
  decypted_id = jwt.decode(request.headers['Authorization'], os.environ.get('JWT_SECRET'), algorithms=['HS256'])['user_id']
  user = models.User.query.filter_by(id=decypted_id).first()
  if request.method == 'PUT':
    user.name = request.json['name']
    user.username = request.json['username']
    user.email = request.json['email']
    models.db.session.add(user)
    models.db.session.commit()
    return {'user' : user.to_json()}
  elif request.method == 'DELETE':
    models.db.session.delete(user)
    models.db.session.commit()
    return {'message' : 'User deleted'}
app.route('/user', methods=['PUT', 'DELETE'])(user_func)


# --- ROUTINE ROUTES ---
# Create routine - POST - /routine - Tested? OK
# Get all routines for user - GET - /routine - Tested? OK
def routine_func():
  decypted_id = jwt.decode(request.headers['Authorization'], os.environ.get('JWT_SECRET'), algorithms=['HS256'])['user_id']
  user = models.User.query.filter_by(id=decypted_id).first()
  if request.method == 'POST':
    routine = models.Routine(
      name = request.json['name'],
      type = request.json['type'],
      user_id = decypted_id
    )
    models.db.session.add(routine)
    models.db.session.commit()
    return {'routine' : routine.to_json()}
  elif request.method == 'GET':
    routines = models.Routine.query.filter_by(user_id=decypted_id).all()
    return {'routine' : [r.to_json() for r in routines]}
app.route('/routine', methods=['POST', 'GET'])(routine_func)

# Get all exercises for routine - GET - /routine/:routine_id - Tested? OK
# Update routine info - PUT - /routine/:routine_id - Tested? OK
# Delete routine - DELETE - /routine/:routine_id - Tested? OK
def routine_id_func(routine_id):
  routine = models.Routine.query.filter_by(id=routine_id).first()
  if request.method == 'GET':
    workouts = models.Workout.query.filter_by(routine_id=routine_id).all()
    return {
      'routine' : routine.to_json(),
      'workout' : [w.to_json() for w in workouts]
      }
  elif request.method == 'PUT':
    routine.name = request.json['name']
    routine.type = request.json['type']
    models.db.session.add(routine)
    models.db.session.commit()
    return {'routine' : routine.to_json()}
  elif request.method == 'DELETE':
    models.db.session.delete(routine)
    models.db.session.commit()
    return {'message':'Routine deleted'}
app.route('/routine/<int:routine_id>', methods=['GET', 'PUT', 'DELETE'])(routine_id_func)

# --- WORKOUT ROUTES ---
# Add exercises to routine - POST - /workout - Tested? OK
def workout_func():
  if request.method == 'POST':
    workout = models.Workout(
      sets = request.json['sets'],
      reps = request.json['reps'],
      rest = request.json['rest'],
      routine_id = request.json['routine_id'],
      exercise_id = request.json['exercise_id']
    )
    models.db.session.add(workout)
    models.db.session.commit()
    return {'workout' : workout.to_json()}
app.route('/workout', methods=['POST'])(workout_func)

# Get all logs for workout - GET - /log - Tested? OK
# Update target sets/reps - PUT - /workout/:workout_id - Tested? OK
# Delete target sets/reps - DELETE  - /workout/:workout_id - Tested? OK
def workout_id_func(workout_id):
  workout = models.Workout.query.filter_by(id=workout_id).first()
  if request.method == 'GET':
    logs = models.Log.query.filter_by(workout_id=workout_id).all()
    return {
      'workout' : workout.to_json(),
      'log' : [l.to_json() for l in logs]
      }
  elif request.method == 'PUT':
    workout.sets = request.json['sets']
    workout.reps = request.json['reps']
    workout.rest = request.json['rest']
    models.db.session.add(workout)
    models.db.session.commit()
    return {'workout' : workout.to_json()}
  elif request.method == 'DELETE':
    models.db.session.delete(workout)
    models.db.session.commit()
    return {'message':'Workout deleted'}
app.route('/workout/<int:workout_id>', methods=['GET', 'PUT', 'DELETE'])(workout_id_func)


# --- LOG ROUTES ---
# Create log - POST - /log - Tested?
def log_func():
    log = models.Log(
      date = datetime.datetime.now().date(),
      # time = datetime.datetime.now().time(),
      workout_id = request.json['workout_id']
    )
    models.db.session.add(log)
    models.db.session.commit()
    return {'log' : log.to_json()}
app.route('/log', methods=['POST'])(log_func)

# Get all entries for log - GET - /log/:log_id - Tested?
# Delete log - DELETE - /log/:log_id - Tested?
def log_id_func(log_id):
  log = models.Log.query.filter_by(id=log_id).first()
  if request.method == 'GET':
    entries = models.Entry.query.filter_by(log_id=log_id).all()
    return {
      'log' : log.to_json(),
      'entry' : [e.to_json() for e in entries]
    }
  elif request.method == 'DELETE':
    models.db.session.delete(log)
    models.db.session.commit()
    return {'message' : 'Log deleted'}
app.route('/log/<int:log_id>', methods=['GET', 'DELETE'])(log_id_func)

# --- ENTRY ROUTES ---
# Create entry - POST - /entry - Tested?
def entry_func():
  entry = models.Entry(
    sets = request.json['sets'],
    reps = request.json['reps'],
    weight = request.json['weight'],
    exercise_id = request.json['exercise_id'],
    log_id = request.json['log_id']
  )
  models.db.session.add(entry)
  models.db.session.commit()
  return {'entry' : entry.to_json()}
app.route('/entry', methods=['POST'])(entry_func)

# Update entry - PUT - /entry/:entry_id - Tested? OK
# Delete entry - DELETE - /entry/:entry_id - Tested? OK
def entry_id_func(entry_id):
  entry = models.Entry.query.filter_by(id=entry_id).first()
  if request.method == 'PUT':
    entry.sets = request.json['sets']
    entry.reps = request.json['reps']
    entry.weight = request.json['weight']
    models.db.session.add(entry)
    models.db.session.commit()
    return {
      'entry' : entry.to_json()
      }
  elif request.method == 'DELETE':
    models.db.session.delete(entry)
    models.db.session.commit()
    return {'message' : 'Entry deleted'}
app.route('/entry/<int:entry_id>', methods=['PUT', 'DELETE'])(entry_id_func)

# --- MISC ROUTES ---
# Test the database works at all - GET - /db_test - Tested? OK
def db_test():
  test1 = models.User(
    name='Test NAME',
    username='Test USERNAME',
    email='Test EMAIL',
    password='123'
  )
  models.db.session.add(test1)
  models.db.session.commit()
  return {
    'test1' : test1.to_json()
  }
app.route('/db_test', methods=['GET'])(db_test)

# Get exercise databse - GET - /exercise - Tested? OK
def get_exercises():
  exercises = models.Exercise.query.all()
  return {'exercises' : [e.to_json() for e in exercises]}
app.route('/exercise', methods=['GET'])(get_exercises)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

  {
    "name" : "TEST Name",
    "username" : "TEST Username",
    "email" : "test@test.com",
    "password" : "123",
    "type" : "TEST Type",
    "sets" : 1,
    "reps" : 1,
    "rest" : 1,
    "weight" : 1,
    "routine_id" : 1,
    "exercise_id" : 1,
    "workout_id" : 2,
    "log_id": 1
}