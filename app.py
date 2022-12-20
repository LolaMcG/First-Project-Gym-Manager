from flask import Flask, render_template

from controllers.exercise_controller import exercises_blueprint
from controllers.client_controller import clients_blueprint
from controllers.booking_controller import bookings_blueprint



app = Flask(__name__)

app.register_blueprint(exercises_blueprint)
app.register_blueprint(clients_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)