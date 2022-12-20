from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
import repos.exercise_repo as exercise_repo
import repos.client_repo as client_repo
import repos.booking_repo as booking_repo

exercises_blueprint = Blueprint("exercises", __name__)

@exercises_blueprint.route("/exercises")
def all_classes():
    exercises = exercise_repo.select_all()
    return render_template("exercises/index.html", exercises = exercises)


@exercises_blueprint.route("/exercises/<id>")
def single_class(id):
    exercises = exercise_repo.select_exercise(id)
    clients = client_repo.select_client(id)
    return render_template("exercises/single_exercise.html", exercises = exercises, clients = clients)