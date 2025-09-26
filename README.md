# PHR-Backend

A backend system for a **Personal Health Record (PHR)** application. This project powers a platform where patients can register, store health data, and collaborate with doctors and medical providers in a secure, privacy-preserving way.

---

## Features

- **Patient Management**: Register patients and securely store their data.
- **Doctor Management**: Add doctors with their specialization and contact details.
- **Treatment Records**: Link doctors to patients through treatments and securely store
    medical notes.
- **SQLite Database**: Lightweight database for fast prototyping and hackathon MVPs.
- **REST API**: Exposes endpoints for patients, doctors, and treatments.

---

## Tech Stack

- **Backend Framework**: Python, Flask  
- **Database**: SQLite with SQLAlchemy ORM  
- **API Style**: RESTful  
- **Environment**: Virtualenv for isolated Python dependencies  

---

## File Structure

```
PHR-Backend/
│── app.py
│── models/
│   ├── __init__.py
│   ├── patients.py
│   ├── doctors.py
│   └── treatments.py
│── routes/
│   ├── patients.py
│   ├── doctors.py
│   └── treatments.py
│── phr.db
│── requirements.txt
│── README.md
```

## Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/Private-Health-Record/PHR-Backend.git
cd PHR-Backend
```

## Setup Instructions

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```
