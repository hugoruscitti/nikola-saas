from flask import Flask
from flask import render_template

app = Flask(__name__)

def helper_include_js(url, basepath='/static/js/', *k, **kv):
    return "<script src='{basepath}{url}' type='text/javascript'></script>".format(url=url, basepath=basepath)

@app.context_processor
def helpers_personalizados():
    return {'include_js': helper_include_js}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/activities")
def activities():
    return render_template("activities.html")

if __name__ == "__main__":
    app.run(debug=True)
