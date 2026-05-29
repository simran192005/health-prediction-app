from flask import Flask, render_template,request ,redirect
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db= SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    full_name = db.Column(db.String(100))
    dob=db.Column(db.String(50))
    email = db.Column(db.String(100))
    glucose = db.Column(db.Float)
    hemoglobin = db.Column(db.Float)
    cholesterol = db.Column(db.Float)
    remarks = db.Column(db.String(200))

@app.route('/')
def home():
    patients= Patient.query.all()
    return render_template('index.html',patients=patients)

@app.route('/add', methods=['POST'])
def add_patient():
    full_name = request.form['full_name']
    dob = request.form['dob']
    email = request.form['email']

    glucose = float(request.form['glucose'])
    hemoglobin = float(request.form['hemoglobin'])
    cholesterol = float(request.form['cholesterol'])

    if glucose>180 and cholesterol>240:
        remarks="High Risk of Diabetes and Heart Disease"
    elif glucose>140:
        remarks="High Diabetes Risk"
    elif cholesterol>240:
        remarks="High Cholesterol Risk"
    elif hemoglobin<12:
        remarks="Possible Anemia"
    else:
        remarks= "Normal"
    
    new_patient =Patient(
        full_name=full_name,
        dob=dob,
        email=email,
        glucose=glucose,
        hemoglobin=hemoglobin,
        cholesterol=cholesterol,
        remarks=remarks
    )

    db.session.add(new_patient)
    db.session.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_patient(id):
    patient = Patient.query.get(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_patient(id):
    patient= Patient.query.get(id)
    if request.method == "POST":
        patient.full_name = request.form['full_name']
        patient.dob = request.form['dob']
        patient.email = request.form['email']
        patient.glucose = float(request.form['glucose'])
        patient.hemoglobin = float(request.form['hemoglobin'])
        patient.cholesterol = float(request.form['cholesterol'])

        if patient.glucose > 180 and patient.cholesterol > 240:
            patient.remarks = "High Risk of Diabetes and Heart Disease"

        elif patient.glucose > 140:
            patient.remarks = "Possible Diabetes Risk"

        elif patient.cholesterol > 240:
            patient.remarks = "High Cholesterol Risk"

        elif patient.hemoglobin < 12:
            patient.remarks = "Possible Anaemia"

        else:
            patient.remarks = "Normal"

        db.session.commit()
        return redirect('/')
    return render_template('edit.html', patient=patient)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)