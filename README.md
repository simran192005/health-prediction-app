# Health Prediction Application

## Overview

This project is a Flask-based Health Prediction Application developed using Python, SQLite, HTML, and Bootstrap.

The application allows users to manage patient health records and predicts possible health risks based on blood test values such as glucose, hemoglobin, and cholesterol.

---

## Features

* Add Patient Records
* View Patient Records
* Update Patient Records
* Delete Patient Records
* Health Risk Prediction
* SQLite Database Integration
* Responsive User Interface

---

## Technologies Used

* Python
* Flask
* Flask SQLAlchemy
* SQLite
* HTML
* Bootstrap

---

## Health Prediction Logic

The system predicts possible conditions such as:

* Diabetes Risk
* High Cholesterol Risk
* Anaemia Risk

based on blood parameter thresholds.

---

## Project Structure

health_prediction_app/
│
├── app.py
├── README.md
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── edit.html

---

## How to Run

Install dependencies:

pip install flask flask_sqlalchemy

Run the application:

python app.py

Open browser:

http://127.0.0.1:5000

---

## Future Improvements

* Real Machine Learning Model Integration
* Authentication System
* Cloud Deployment
* Data Visualization Dashboard
* External Healthcare API Integration

