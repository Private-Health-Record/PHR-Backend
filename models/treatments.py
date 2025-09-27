from . import db

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    comments = db.Column(db.String(500), nullable=True)
    diagnosis = db.Column(db.String(250), nullable=True)
    medications = db.Column(db.Text, nullable=True)
    procedure = db.Column(db.String(250), nullable=True)
    follow_up_date = db.Column(db.DateTime, nullable=True)
    attachments_url = db.Column(db.String(250), nullable=True)
    status = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "comments": self.comments,
            "diagnosis": self.diagnosis,
            "medications": self.medications,
            "procedure": self.procedure,
            "date": self.date.strftime("%Y-%m-%d %H:%M") if self.date else None,
            "follow_up_date": self.follow_up_date.strftime("%Y-%m-%d %H:%M") if self.follow_up_date else None,
            "attachments_url": self.attachments_url,
            "status": self.status
        }
