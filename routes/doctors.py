from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models import db
from models.doctors import Doctor

doctor_routes = Blueprint("doctors", __name__)

@doctor_routes.route("", methods=["POST"])  
@cross_origin(origin="http://localhost:3000")  
def add_doctor():
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")
    specialization = data.get("specialization")
    contact = data.get("contact")
    name = data.get("name")



    if not (name and specialization and contact):
        return jsonify({"error": "Missing required fields"}), 400


    existing = Doctor.query.filter_by(contact=contact).first()
    if existing:
        return jsonify({"error": "Doctor with this contact already exists"}), 400

    new_doctor = Doctor( email=email, specialization = specialization, contact = contact)
    db.session.add(new_doctor)    
    db.session.commit()


    return jsonify({
        "status": "doctor added",
        "doctor": new_doctor.to_dict()  # use your model’s to_dict()
    }), 201

@doctor_routes.route("/", methods=["GET"])
def list_doctors():
    doctors = Doctor.query.all()
    return jsonify([doc.to_dict() for doc in doctors]), 200
