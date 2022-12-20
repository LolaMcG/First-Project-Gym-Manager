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


@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking = booking_repo.select_booking(id)
    client_id = booking.client.id
    booking_repo.delete_single(id)
    return redirect (f"/clients/{client_id}")