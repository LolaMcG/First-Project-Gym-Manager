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

def client_for_booking(booking):
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [booking.client.id]
    results = run_sql(sql, values)
    for row in results:
        client = Client(row['first_name'], row['last_name'], row['phone_no'], row['gender'], row['medi_cond'], row['id'])
        return client

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)

def delete_client(id):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql, values)