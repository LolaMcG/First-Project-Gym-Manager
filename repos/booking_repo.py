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


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for each_booking in results:
        client = client_repo.select_client(each_booking['client_id'])
        exercise = exercise_repo.select_exercise(each_booking['exercise_id'])
        booking = Booking(client, exercise, each_booking['id'])
        bookings.append(booking)
    return bookings


def select_booking(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        client = client_repo.select_client(result['client_id'])
        exercise = exercise_repo.select_exercise(result['exercise_id'])
        booking = Booking(client, exercise, id)
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete_single(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_bookings_by_client_id(client_id):
    bookings = []
    sql ="SELECT * FROM bookings WHERE client_id = %s"
    values = [client_id]
    results = run_sql(sql, values)

    client = client_repo.select_client(client_id)

    for each_booking in results:
        exercise = exercise_repo.select_exercise(each_booking['exercise_id'])
        booking = Booking(client, exercise, each_booking['id'])
        bookings.append(booking)
    return bookings

def select_bookings_by_exercise_id(exercise_id):
    bookings = []
    sql = "SELECT * FROM bookings WHERE exercise_id = %s"
    values = [exercise_id]
    results = run_sql(sql, values)
    exercise = exercise_repo.select_exercise(exercise_id)
    
    for each_booking in results:
        client = client_repo.select_client(each_booking['client_id'])
        booking = Booking(client, exercise, each_booking['id'])
        bookings.append(booking)
    return bookings
