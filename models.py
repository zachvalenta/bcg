from app import db


class Pet(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(80))
    breed = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    name = db.Column(db.String(80))
    age = db.Column(db.String(20))
    zip_code = db.Column(db.String(20))

    def __repr__(self):
        return f"""id {self.pet_id} species {self.species}
            breed {self.breed} gender {self.gender} name {self.name}
            age {self.age} zip code {self.zip_code}"""
