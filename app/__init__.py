from flask import Flask, redirect
from .views.home import home
from .views.solution_templates import solution_templates


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")  # instance/config.py
app.register_blueprint(home)
app.register_blueprint(solution_templates)


@app.route("/", methods=["GET"])
def index_page():
    return redirect("/home")
