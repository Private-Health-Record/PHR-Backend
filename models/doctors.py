from . import db

class Doctor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    specialization = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(80), unique=True, nullable=False)
    treatments = db.relationship("Treatment", backref="doctor", lazy=True)

    hospital = db.Column(db.String(40), nullable=False)              
    intro = db.Column(db.Text, nullable=True)                         
    experience = db.Column(db.Integer, nullable=False)                 
    availability_from = db.Column(db.Time, nullable=True)             
    availability_to = db.Column(db.Time, nullable=True)               
    profile_pic_url = db.Column(db.String(250), nullable=True)        

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "contact": self.contact,
            "hospital": self.hospital,
            "intro": self.intro,
            "experience": self.experience,
            "availability_from": self.availability_from.strftime("%H:%M") if self.availability_from is not None else None,
            "availability_to": self.availability_to.strftime("%H:%M") if self.availability_to is not None else None,
            "profile_pic_url": self.profile_pic_url
        }
