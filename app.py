from flask import Flask

from controllers.exercises_controller import bootcamps_blueprint

app = Flask(__name__)

app.register_blueprint(bootcamps_blueprint)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug-True)