from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models import db
from models.doctors import Doctor

doctor_routes = Blueprint("doctors", __name__)

@doctor_routes.route("/", methods=["POST"])  
@cross_origin(origin="http://localhost:3000")  
def add_doctor():
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")


    if not all([email, password]):
        return jsonify({"error": "Missing required fields: email, password"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400


    existing = Doctor.query.filter_by(email=email).first()
    if existing:
        return jsonify({"error": "Doctor with this email already exists"}), 400

    new_doctor = Doctor(
        email=email, 
    )
    new_doctor.set_password(password)
    
    db.session.add(new_doctor)  
    db.session.commit()

    return jsonify({
        "status": "doctor added successfully",
        "doctor": {
            "id": new_doctor.id, 
            "email": new_doctor.email,
            "name": f"{new_doctor.first_name} {new_doctor.last_name}"
        } 
    }), 201