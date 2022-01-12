import os
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
  try:
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
  except:
    return { 'message' : 'Email must be present and unique' }, 400
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
      sets = request.json['sets'],
      reps = request.json['reps'],
      rest = request.json['rest'],
      exercise_id = request.json['exercise_id'],
      user_id = decypted_id
    )
    models.db.session.add(routine)
    models.db.session.commit()
    return {'routine' : routine.to_json()}
  elif request.method == 'GET':
    routines = models.Routine.query.filter_by(user_id=decypted_id).all()
    return {'routine' : [r.to_json() for r in routines]}
app.route('/routine', methods=['POST', 'GET'])(routine_func)

# Get routine info - GET - /routine/:routine_id - Tested?
# Update routine info - PUT - /routine/:routine_id - Tested?
# Delete routine - DELETE - /routine/:routine_id - Tested?
def routine_id_func(routine_id):
  if request.method == 'GET':
    pass
  elif request.method == 'PUT':
    pass
  elif request.method == 'DELETE':
    routine = 
  return 'OK'
app.route('/routine/<int:routine_id>', methods=['GET', 'PUT', 'DELETE'])(routine_id_func)

# --- WORKOUT ROUTES ---
# Create workout log - POST - /workout - Tested?
# Get all workout logs - GET - /workout - Tested?
# NOTE: Do I actually need this route?

# Get individual workout log - GET - /workout/:workout_id - Tested?
# Delete workout log - DELETE - /workout/:workout_id - Tested?

# Create log under workout - POST - /workout/:workout_id/log - Tested?
# Get all logs under workout - GET - /workout/:workout_id/log - Tested?

# Update log under workout - PUT - /workout/:workout_id/log/:log_id - Tested?
# Delete log under workout - DELETE - /workout/:workout_id/log/:log_id - Tested?

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