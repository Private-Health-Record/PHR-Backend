from flask import Blueprint, request, jsonify
from models import db
from models.treatments import Treatment
from models.patients import Patient
from models.doctors import Doctor

treatment_routes = Blueprint("treatments", __name__)

# POST /treatments
@treatment_routes.route("", methods=["POST"])
def add_treatment():
    data = request.get_json()
    patient_id = data.get("patient_id")
    doctor_id = data.get("doctor_id")
    comments = data.get("comments")

    if not (patient_id and doctor_id and comments):
        return jsonify({"error": "Missing fields"}), 400

    # validate patient & doctor exist
    if not Patient.query.get(patient_id):
        return jsonify({"error": "Patient not found"}), 404
    if not Doctor.query.get(doctor_id):
        return jsonify({"error": "Doctor not found"}), 404

    new_treatment = Treatment(
        patient_id=patient_id,
        doctor_id=doctor_id,
        comments=comments
    )
    db.session.add(new_treatment)
    db.session.commit()

    return jsonify({
        "status": "treatment added",
        "treatment": {
            "id": new_treatment.id,
            "patient_id": new_treatment.patient_id,
            "doctor_id": new_treatment.doctor_id,
            "comments": new_treatment.comments
        }
    }), 201


# GET /treatments/patient/<id>
@treatment_routes.route("/patient/<int:patient_id>", methods=["GET"])
def get_treatments_for_patient(patient_id):
    treatments = Treatment.query.filter_by(patient_id=patient_id).all()
    return jsonify([
        {
            "id": t.id,
            "doctor_id": t.doctor_id,
            "comments": t.comments
        } for t in treatments
    ]), 200


# GET /treatments
@treatment_routes.route("/", methods=["GET"])
def list_treatments():
    treatments = Treatment.query.all()
    return jsonify([
        {
            "id": t.id,
            "patient_id": t.patient_id,
            "doctor_id": t.doctor_id,
            "comments": t.comments
        } for t in treatments
    ]), 200
