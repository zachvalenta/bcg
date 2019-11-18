#!/usr/bin/env python

from app import db
from models import Pet

print("\n ⤵️  sample queries \n\n")
print(f" 🔍 get all pets: `Pet.query.all()` --> {Pet.query.all()} \n")
