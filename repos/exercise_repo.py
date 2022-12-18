from db.run_sql import run_sql

from models.exercise import Exercise
from models.client import Client

def save(exercise):
    sql = "INSERT INTO exercises (description, capacity, instructor, time, location) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [exercise.description, exercise._capacity, exercise.instructor, exercise.time, exercise.location]
    results = run_sql(sql, values)
    exercise.id = results[0]['id']
    return exercise

def delete_all():
    sql = "DELETE FROM exercises"
    run_sql(sql)