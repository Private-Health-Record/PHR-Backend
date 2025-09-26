from . import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    health_data = db.relationship("HealthData", backref="patient", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "health_data": [d.to_dict() for d in self.health_data]
        }


class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(500), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "entry": self.entry,
            "patient_id": self.patient_id
        }
