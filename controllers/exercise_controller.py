from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
import repos.exercise_repo as exercise_repo
import repos.client_repo as client_repo

exercises_blueprint = Blueprint("exercises", __name__)

