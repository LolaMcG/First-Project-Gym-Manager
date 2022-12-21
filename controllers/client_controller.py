from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo
import repos.booking_repo as booking_repo

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def all_clients():
    clients = client_repo.select_all()
    return render_template("clients/index.html", clients = clients)

# /clients/ whatever 
@clients_blueprint.route("/clients/<id>")
def single_client(id):
    client = client_repo.select_client(id)
    bookings = booking_repo.select_bookings_by_client_id(id)
    return render_template("clients/single_client.html", client=client, bookings = bookings)

@clients_blueprint.route("/clients/new")
def new_client():
    return render_template("clients/new_client.html")


@clients_blueprint.route("/clients", methods=["POST"])
def add_new_client():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    phone_no = request.form["phone"]
    gender = request.form["gender"]
    medi_cond = request.form["medical"]
    new_client = Client(first_name, last_name, phone_no, gender, medi_cond)
    client_repo.save(new_client)
    return redirect ("/clients")


@clients_blueprint.route("/clients/<id>/edit")
def edit_client(id):
    client = client_repo.select_client(id)
    return render_template("clients/edit.html", client = client)


@clients_blueprint.route("/clients/<id>", methods=["POST"])
def update(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    phone_no = request.form["phone"]
    gender = request.form["gender"]
    medi_cond = request.form["medical"]
    new_client = Client(first_name, last_name, phone_no, gender, medi_cond, id)
    client_repo.update_client(new_client)
    return redirect("/clients")