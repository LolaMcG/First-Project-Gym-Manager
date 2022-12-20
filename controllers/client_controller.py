from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def all_clients():
    clients = client_repo.select_all
    return render_template("clients/index.html", clients = clients)
