from db.run_sql import run_sql

from models.client import Client
from models.exercise import Exercise
from models.booking import Booking
import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo

def save(booking):
    sql = "INSERT INTO bookings (client_id, exercise_id) VALUES (%s, %s) RETURNING id"
    values = [booking.client.id, booking.exercise.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking