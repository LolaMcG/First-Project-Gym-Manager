from db.run_sql import run_sql

from models.client import Client
from models.exercise import Exercise

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, phone_no, gender, medi_cond) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [client.first_name, client.last_name, client.phone_no, client.gender, client.medi_cond]
    results = run_sql(sql, values)
    client.id = results[0]['id']
    return client

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)