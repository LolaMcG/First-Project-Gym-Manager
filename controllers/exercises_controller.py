from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Bootcamp
import repos.exercise_repo as exercise_repo
import repos.client_repo as client_repo

bootcamps_blueprint = Blueprint("bbg", __name__)


