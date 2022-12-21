from db.run_sql import run_sql

from models.exercise import Exercise
from models.client import Client

def save(exercise):
    sql = "INSERT INTO exercises (description, capacity, instructor, time, location) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [exercise.description, exercise._capacity, exercise.instructor, exercise.time, exercise.location]
    results = run_sql(sql, values)
    exercise.id = results[0]['id']
    return exercise


def select_all():
    exercises = []
    sql = "SELECT * FROM exercises"
    results = run_sql(sql)
    for each_exercise in results:
        exercise = Exercise(each_exercise['description'], each_exercise['capacity'], each_exercise['instructor'], each_exercise['time'], each_exercise['location'], each_exercise['id'])
        exercises.append(exercise)
    return exercises


def select_exercise(id):
    exercise = None
    sql = "SELECT * FROM exercises WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        exercise = Exercise(result['description'], result['capacity'], result['instructor'], result['time'], result['location'], result['id'])
    return exercise


def exercises_for_clients(client):
    exercises = []
    sql = "SELECT exercises.* FROM exercises INNER JOIN bookings ON bookings.exercise_id = exercises.id WHERE client_id = %s"
    values = [client.id]
    results = run_sql(sql, values)
    for each_row in results:
        exercise = Exercise(each_row['description'], each_row['capacity'], each_row['instructor'], each_row['time'], each_row['location'], each_row['id'])
        exercises.append(exercise)
    return exercises


def exercise_for_booking(booking):
    sql = "SELECT * FROM exercises WHERE id = %s"
    values = [booking.exercise.id]
    results = run_sql(sql, values)
    for row in results:
        exercise = Exercise(row['description'], row['capacity'], row['instructor'], row['time'], row['location'], row['id'])
        return exercise


def update_exercise(exercise):
    sql = "UPDATE exercises SET description = %s, capacity = %s, instructor = %s, time = %s, location = %s WHERE id = %s"
    values = [exercise.description, exercise._capacity, exercise.instructor, exercise.time, exercise.location, exercise.id]
    run_sql(sql, values)


def delete_exercise(id):
    sql = "DELETE FROM exercises WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM exercises"
    run_sql(sql)