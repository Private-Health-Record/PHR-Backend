from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import models so they register with SQLAlchemy
from .patients import Patient, HealthData
from .doctors import Doctor
from .treatments import Treatment
