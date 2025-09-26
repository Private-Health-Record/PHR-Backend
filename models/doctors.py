from . import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(120), unique=True, nullable=False)
    treatments = db.relationship("Treatment", backref="doctor", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "contact": self.contact
        }
