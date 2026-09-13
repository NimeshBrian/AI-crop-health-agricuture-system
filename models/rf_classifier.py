import warnings
warnings.filterwarnings('ignore')
import joblib
import numpy as np
import os

# Define relative path to the trained Random Forest model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'saved', 'rf_irrigation_model.pkl')

# Load the saved model
rf_model = joblib.load(MODEL_PATH)

def predict_irrigation(soil_moisture, temperature, humidity, rainfall):
    """
    Takes sensor inputs and returns the predicted irrigation requirement:
    Returns: 'Low', 'Medium', or 'High'
    """
    input_features = np.array([[soil_moisture, temperature, humidity, rainfall]])
    prediction = rf_model.predict(input_features)
    return prediction[0]

if __name__ == "__main__":
    # Test sample with low moisture to verify prediction logic
    sample_moisture = 20.0
    sample_temp = 32.0
    sample_humidity = 45.0
    sample_rain = 0.0

    result = predict_irrigation(sample_moisture, sample_temp, sample_humidity, sample_rain)
    print("Random Forest Irrigation model loaded successfully.")
    print(f"Sample Test -> Moisture: {sample_moisture}%, Temp: {sample_temp}C | Recommendation: {result}")