from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Hello World"})

patient_info = []
doctor_info = []
treatment = []

#patient info
@app.route("/add_patient", methods=["POST"])
def add_patient():
    data = request.get_json()

    name = data.get("patient_name")
    age = data.get("patient_age")
    gender = data.get("patient_gender")
    contact = data.get("patient_contact")
    ciphertext = data.get("ciphertext")  

    if not (name and age and gender and contact and ciphertext):
        return jsonify({"error": "Missing fields"}), 400

    patient = {
        "id": len(patient_info) + 1,
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact,
        "encrypted_info": ciphertext
    }
    patient_info.append(patient)

    return jsonify({"status": "stored", "patient": patient}), 201


#doctor info
@app.route("/add_doctor", methods=["POST"])
def add_doctor():
    data = request.get_json()
    name = data.get("doctor_name")
    specialization = data.get("specialization")
    contact = data.get("doctor_contact")

    if not (name and specialization and contact):
        return jsonify({"error": "Missing fields"}), 400

    doctor = {
        "id": len(doctor_info) + 1,
        "name": name,
        "specialization": specialization,
        "contact": contact
    }
    doctor_info.append(doctor)

    return jsonify({"status": "stored", "doctor": doctor}), 201


# doctor treatment comments
@app.route("/add_treatment", methods=["POST"])
def add_treatment():
    data = request.get_json()
    patient_id = data.get("patient_id")
    doctor_id = data.get("doctor_id")
    comments = data.get("comments")
    ciphertext = data.get("ciphertext") 

    if not (patient_id and doctor_id and comments and ciphertext):
        return jsonify({"error": "Missing fields"}), 400

    treatment = {
        "id": len(treatment) + 1,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "comments": comments,
        "encrypted_info": ciphertext
    }
    treatment.append(treatment)

    return jsonify({"status": "stored", "treatment": treatment}), 201


# Get patient info (demo)
@app.route("/patients", methods=["GET"])
def get_patients():
    return jsonify(patient_info), 200


# Get treatments for a patient
@app.route("/treatments/<int:patient_id>", methods=["GET"])
def get_treatments(patient_id):
    patient_treatments = [t for t in treatment if t["patient_id"] == patient_id]
    return jsonify(patient_treatments), 200



if __name__ == "__main__":
    app.run(debug=True)
