from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/create")
def create():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)
