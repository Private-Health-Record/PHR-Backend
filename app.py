from flask import Flask
from models import db
from flask_cors import CORS 
from models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///phr.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app, origins=["http://localhost:3000"])

    db.init_app(app)

    # Register blueprints
    from routes.patients import patient_routes
    from routes.doctors import doctor_routes
    from routes.treatments import treatment_routes

    app.register_blueprint(patient_routes, url_prefix="/patients")
    app.register_blueprint(doctor_routes, url_prefix="/doctors")
    app.register_blueprint(treatment_routes, url_prefix="/treatments")

    @app.route("/")
    def home():
        return {"status": "ok", "message": "Welcome to PHR Backend"}

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
