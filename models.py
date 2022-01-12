from sqlalchemy.sql.schema import ForeignKey
from flask_academy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  username = db.Column(db.String, unique=True, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)

  # User associations
  routine_rel = db.relationship('Routine')

  def to_json(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'username' : self.username,
      'email' : self.email
    }

class Exercise(db.Model):
  __tablename__ = 'exercises'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  category = db.Column(db.String)
  primaryMuscles = db.Column(db.ARRAY(db.String))
  secondaryMuscles = db.Column(db.ARRAY(db.String))

  # Exercise associations
  routine_rel = db.relationship('Routine')
  log_re = db.relationship('Log')

  def to_json(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'primaryMuscles' : self.primaryMuscles,
      'secondaryMuscles' : self.secondaryMuscles
    }

class Routine(db.Model):
  __tablename__ = 'routines'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  type = db.Column(db.String)
  sets = db.Column(db.Integer)
  reps = db.Column(db.Integer)
  rest = db.Column(db.Integer)

  # Routine associations
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
  workout_rel = db.Relationship('Workout')

  def to_json(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'type' : self.type,
      'sets' : self.sets,
      'reps' : self.reps,
      'rest' : self.rest
    }

class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  start_time = db.Column(db.Time)

  # Workout associations
  routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'))
  log_rel = db.relationship('Log')

  def to_json(self):
    return {
      'id' : self.id,
      'date' : self.date,
      'start_time' : self.start_time 
    }

class Log(db.Model):
  __tablename__ = 'logs'

  id = db.Column(db.Integer, primary_key=True)
  sets = db.Column(db.Integer, nullable=False)
  reps = db.Column(db.Integer, nullable=False)
  weight = db.Column(db.Integer, nullable=False)
  exercise_time = db.Column(db.Time)

  # Log assocation
  workout_id = db.Column(db.Integer, ForeignKey('workouts.id'))
  exercise_id = db.Column(db.Integer, ForeignKey('exercises.id'))

  def to_json(self):
    return {
      'id' : self.id,
      'sets' : self.sets,
      'reps' : self.reps,
      'weight' : self.weight,
      'exercise_time' : self.exercise_time
    }