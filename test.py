import joblib
import pandas as pd

# Load the model
model = joblib.load("app/ml_model/lung_cancer_model.pkl")

# Define sample input data
sample_input= {
  "GENDER": 1,
  "AGE": 70,
  "SMOKING": 2,
  "YELLOW_FINGERS": 2,
  "ANXIETY": 2,
  "PEER_PRESSURE": 2,
  "CHRONIC DISEASE": 2,
  "FATIGUE ": 2,
  "ALLERGY ": 2,
  "WHEEZING": 2,
  "ALCOHOL CONSUMING": 2,
  "COUGHING": 2,
  "SHORTNESS OF BREATH": 2,
  "SWALLOWING DIFFICULTY": 2,
  "CHEST PAIN": 2
}
# Convert to DataFrame
input_df = pd.DataFrame([sample_input])

# Make prediction
prediction = model.predict(input_df)
print("Prediction:", prediction)