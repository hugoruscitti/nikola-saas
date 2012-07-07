import os
from flask import Flask
from flask import render_template
from flask import request
import commands
import utils


app = Flask(__name__)
sites_path = "./sites/"

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
    name = os.path.basename(url)
    result = commands.clonar_repositorio(url, sites_path + name)
    return render_template("create_site.html", result=result)

@app.route("/activities")
def activities():
    return render_template("activities.html")

@app.route("/update/<site>")
def update(site):
    url = utils.get_url_from_repository(os.path.join(sites_path, site))
    return clone_site(url)

if __name__ == "__main__":
    app.run(debug=True)
