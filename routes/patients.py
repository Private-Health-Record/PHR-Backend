from flask import Blueprint, request, jsonify
from models import db
from models.patients import Patient, HealthData

patient_routes = Blueprint("patient_routes", __name__)

# POST /patients
@patient_routes.route("", methods=["POST"])   # no trailing slash
def add_patient():
    data = request.get_json()
    patient = Patient(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify({"message": "Patient registered successfully"}), 201


# POST /patients/<id>/add_data
@patient_routes.route("/<int:patient_id>/add_data", methods=["POST"])
def add_health_data(patient_id):
    data = request.get_json()
    health_entry = data.get("health_entry")

    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    entry = HealthData(entry=health_entry, patient_id=patient.id)
    db.session.add(entry)
    db.session.commit()

    return jsonify({"status": "data added", "patient": patient.to_dict()}), 201


# GET /patients
@patient_routes.route("", methods=["GET"])   # remove the slash
def list_patients():
    patients = Patient.query.all()
    return jsonify([p.to_dict() for p in patients])
