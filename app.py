import os
from flask import Flask
from flask import render_template
from flask import request
from flask.ext.celery import Celery
import commands
import utils


app = Flask(__name__)
app.config.from_pyfile("config.py")
sites_path = "./sites/"

celery = Celery(app)

def helper_include_js(url, basepath='/static/js/', *k, **kv):
    return "<script src='{basepath}{url}' type='text/javascript'></script>".format(url=url, basepath=basepath)

@app.context_processor
def helpers_personalizados():
    return {'include_js': helper_include_js}

@app.route("/")
def list():
    sites = [d for d in os.listdir(sites_path) if os.path.isdir(os.path.join(sites_path, d))]
    return render_template("list.html", sites=sites)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create_site", methods=['POST'])
def create_site():
    url = request.form['url']
    return clone_site(url)

def clone_site(url):
    task = task_clone_site.delay(url)
    return render_template("create_site.html", id=task.task_id)

@celery.task(name="app.clone_site")
def task_clone_site(url):
    name = os.path.basename(url)
    return commands.clonar_repositorio(url, sites_path + name)

@app.route("/activities")
def activities():
    return render_template("activities.html")

@app.route("/update/<site>")
def update(site):
    url = utils.get_url_from_repository(os.path.join(sites_path, site))
    return clone_site(url)

@app.route("/obtener_estado/<id_tarea>")
def obtener_estado(id_tarea):
    t = task_clone_site.AsyncResult(id_tarea)
    return t.status

if __name__ == "__main__":
    app.run(debug=True)
