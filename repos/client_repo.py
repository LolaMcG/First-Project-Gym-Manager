from db.run_sql import run_sql

from models.client import Client
from models.exercise import Exercise

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, phone_no, gender, medi_cond) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [client.first_name, client.last_name, client.phone_no, client.gender, client.medi_cond]
    results = run_sql(sql, values)
    client.id = results[0]['id']
    return client

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    for row in results:
        client = Client(row['first_name'], row['last_name'], row['phone_no'], row['gender'], row['medi_cond'], row['id'])
        clients.append(client)
    return clients
    

def select_client(id):
    client = None
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        client = Client(result['first_name'], result['last_name'], result['phone_no'], result['gender'], result['medi_cond'], result['id'])
    return client

def clients_for_exercises(exercise):
    clients = []
    sql = "SELECT clients.* FROM clients INNER JOIN bookings ON bookings.client_id = clients.id WHERE exercise_id = %s"
    values = [exercise.id]
    results = run_sql(sql, values)

    for row in results:
        client = Client(row['first_name'], row['last_name'], row['phone_no'], row['gender'], row['medi_cond'], row['id'])
        clients.append(client)

    return clients


def exercises_for_clients(client):
    exercises = []
    sql = "SELECT exercises.* FROM exercises INNER JOIN bookings ON bookings.exercise_id = exercise.id WHERE client_id = %s"
    values = [client.id]
    results = run_sql(sql, values)

    for row in results:
        exercise = Exercise(row['description'], row['capacity'], row['instructor'], row['time'], row['location'], row['id'])
        exercises.append(exercise)
    return exercises

def client_for_booking(booking):
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [booking.client.id]
    results = run_sql(sql, values)
    for row in results:
        client = Client(row['first_name'], row['last_name'], row['phone_no'], row['gender'], row['medi_cond'], row['id'])
        return client


def update_client(client):
    sql = "UPDATE clients SET first_name = %s, last_name = %s, phone_no  = %s, gender  = %s, medi_cond = %s WHERE id = %s"
    values = [client.first_name, client.last_name, client.phone_no, client.gender, client.medi_cond, client.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)


def delete_client(id):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql, values)