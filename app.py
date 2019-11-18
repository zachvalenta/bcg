import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, jsonify, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy

"""
CONF
"""

# db - load env, construct path
load_dotenv(find_dotenv())
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, os.getenv("DATABASE"))
db_uri = "sqlite:///" + db_path

# app - init, config
app = Flask(__name__, template_folder=basedir)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

# db - init, ingest models, create db/tables (if they don't already exist)
db = SQLAlchemy(app)
from models import Pet

db.create_all()


"""
ENDPOINTS
"""


@app.route("/")
def get_index():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/pet")
def get_pet_price():
    try:
        pet = Pet.query.filter_by(
            pet_id=request.args.get("id")
        ).first()  # TODO throw exception before calc
        cost = calc(pet)
        return jsonify({"cost": cost})
    except AttributeError:
        return Response("no record with that id", 404)


ages = {"0": 1.01, "1": 1.015, "5": 1.03, "8": 1.044, "9": 1.055}

breeds = {"golden_retriever": 1.01, "ragdoll": 1.002}

species = {"cat": 0.99, "dog": 1}

zip_codes = {"10001": 1.015, "90210": 1.01}


def calc(pet):
    breed = breeds[pet.breed]
    age = ages[pet.age]
    zip_code = zip_codes[pet.zip_code]
    sp = species[pet.species]
    base = 45
    return base * (breed + zip_code + age + sp)
