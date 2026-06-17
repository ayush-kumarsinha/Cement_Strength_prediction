from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

import os

print("Current Working Directory:", os.getcwd())
print("Templates Path Exists:", os.path.exists("templates"))
print("Index Exists:", os.path.exists("templates/index.html"))

model = joblib.load("Model/cement_strength_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['cement']),
        float(request.form['slag']),
        float(request.form['flyash']),
        float(request.form['water']),
        float(request.form['superplasticizer']),
        float(request.form['coarseagg']),
        float(request.form['fineagg']),
        float(request.form['age'])
    ]

    prediction = model.predict([features])

    return render_template(
        'index.html',
        prediction_text=f"Predicted Cement Strength: {prediction[0]:.2f} MPa"
    )

if __name__ == "__main__":
    app.run(debug=True)