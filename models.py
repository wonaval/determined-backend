from flask_sqlalchemy import SQLAlchemy
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
  workout_rel = db.relationship('Workout')
  entry_rel = db.relationship('Entry')

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
  name = db.Column(db.String, unique=True)
  type = db.Column(db.String)

  # Routine associations
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  workout_rel = db.relationship('Workout')

  def to_json(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'type' : self.type
    }

class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  sets = db.Column(db.Integer, nullable=False)
  reps = db.Column(db.Integer, nullable=False)
  rest = db.Column(db.Integer, nullable=False)

  # Workout associations
  routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
  log_rel = db.relationship('Log')

  def to_json(self):
    return {
      'id' : self.id,
      'sets' : self.sets,
      'reps' : self.reps,
      'rest' : self.rest,
      'exercise_id' : self.exercise_id
    }

class Log(db.Model):
  __tablename__ = 'logs'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)

  # Log assocations
  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
  entry_rel = db.relationship('Entry')

  def to_json(self):
    return {
      'id' : self.id,
      'date' : self.date,
      # 'time' : self.time
    }

class Entry(db.Model):
  __tablename__ = 'entries'

  id = db.Column(db.Integer, primary_key=True)
  sets = db.Column(db.Integer, nullable=False)
  reps = db.Column(db.Integer, nullable=False)
  weight = db.Column(db.Integer, nullable=False)

  # Entry assocations
  log_id = db.Column(db.Integer, db.ForeignKey('logs.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

  def to_json(self):
    return {
      'id' : self.id,
      'sets' : self.sets,
      'reps' : self.reps,
      'weight' : self.weight
    }