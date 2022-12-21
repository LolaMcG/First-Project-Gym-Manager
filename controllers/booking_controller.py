from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repos.booking_repo as booking_repo
import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def all_bookings():
    bookings = booking_repo.select_all()
    return render_template("bookings/index.html", bookings = bookings)


@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking = booking_repo.select_booking(id)
    client_id = booking.client.id
    booking_repo.delete_single(id)
    return redirect (f"/clients/{client_id}")

@bookings_blueprint.route("/bookings/new")
def new_booking():
    clients = client_repo.select_all()
    exercises = exercise_repo.select_all()
    return render_template("bookings/new_booking.html", clients = clients, exercises = exercises)

@bookings_blueprint.route("/bookings", methods=["POST"])
def add_booking():
    client_id = request.form['client_id']
    exercise_id = request.form['exercise_id']
    client = client_repo.select_client(client_id)
    exercise = exercise_repo.select_exercise(exercise_id)
    booking = Booking(client, exercise)
    booking_repo.save(booking)
    return redirect("/bookings")