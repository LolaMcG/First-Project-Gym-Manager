from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo

clients_blueprint = Blueprint("clients", __name__)