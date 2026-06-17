# Cement_Strength_prediction

# Cement Strength Prediction

## Project Overview

This project predicts the compressive strength of concrete using Machine Learning. The model is trained on different concrete mixture components such as cement, fly ash, water, superplasticizer, coarse aggregate, fine aggregate, and age of concrete.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Flask
* HTML/CSS
* Joblib

## Workflow

1. Data Collection
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Deployment using Flask

## Model Performance

* Linear Regression R² Score: 0.58
* Random Forest R² Score: 0.91

Random Forest was selected as the final model because it achieved the highest accuracy.

## Input Features

* Cement
* Blast Furnace Slag
* Fly Ash
* Water
* Superplasticizer
* Coarse Aggregate
* Fine Aggregate
* Age

## Output

The application predicts the Concrete Compressive Strength (MPa).

## Project Structure

Cement_Strength_prediction/

├── Dataset/

├── Model/

│ └── cement_strength_model.pkl

├── Notebook/

├── templates/

│ └── index.html

├── static/

├── app.py

├── requirements.txt

└── README.md

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python app.py

3. Open browser:
   http://127.0.0.1:5000

## Author

Ayush Kumar
Data Analyst | Machine Learning Enthusiast
