#!/usr/bin/env python

from app import db
from models import Pet

print("\n 🌱 seeding db... \n")

db.drop_all()
db.create_all()

pets = [
    Pet(
        species="dog",
        breed="golden_retriever",
        gender="female",
        name="lola",
        age="5",
        zip_code="10001",
    ),
    Pet(
        species="cat",
        breed="ragdoll",
        gender="male",
        name="leo",
        age="9",
        zip_code="19320",
    ),
]

db.session.bulk_save_objects(pets)
db.session.commit()

print("\n 🌿 done \n")
print(f"songs {Pet.query.all()} \n")
