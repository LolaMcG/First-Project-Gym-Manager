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
def single_exercise(id):
    exercise = exercise_repo.select_exercise(id)
    bookings = booking_repo.select_bookings_by_exercise_id(id)
    return render_template("exercises/single_exercise.html", exercise = exercise, bookings = bookings)


@exercises_blueprint.route("/exercises/new")
def new_exercise():
    return render_template("exercises/new_exercise.html")


@exercises_blueprint.route("/exercises", methods=["POST"])
def add_new_exercise_class():
    description = request.form["description"]
    capacity = request.form["capacity"]
    instructor = request.form["instructor"]
    time = request.form["time"]
    location = request.form["location"]
    new_exercise_class = Exercise(description, capacity, instructor, time, location)
    exercise_repo.save(new_exercise_class)
    return redirect ("/exercises")

@exercises_blueprint.route("/exercises/<id>/edit")
def edit_exercise(id):
    exercise = exercise_repo.select_exercise(id)
    return render_template("exercises/edit.html", exercise = exercise)