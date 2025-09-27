from . import db

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    health_data = db.relationship("HealthData", backref="patient", lazy=True)

    phone = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    blood_type = db.Column(db.String(5), nullable=False)
    allergies = db.Column(db.Text, nullable=True)
    chronic_conditions = db.Column(db.Text, nullable=True)
    current_medications = db.Column(db.Text, nullable=True)
    profile_pic_url = db.Column(db.String(250), nullable=True)
    
    health_data = db.relationship("HealthData", backref="patient", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "dob": self.dob.strftime("%Y-%m-%d") if self.dob else None,
            "gender": self.gender,
            "blood_type": self.blood_type,
            "allergies": self.allergies,
            "chronic_conditions": self.chronic_conditions,
            "current_medications": self.current_medications,
            "profile_pic_url": self.profile_pic_url,
            "health_data": [d.to_dict() for d in self.health_data]
        }


class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(500), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "symptoms": self.symptoms,
            "entry": self.entry,
            "patient_id": self.patient_id
        }

    


