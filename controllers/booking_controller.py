from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repos.booking_repo as booking_repo
import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo

bookings_blueprint = Blueprint("bookings", __name__)