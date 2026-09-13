import streamlit as st
import pandas as pd
from models.cnn_classifier import predict_disease
from models.rf_classifier import predict_irrigation
from rules.recommendation_engine import get_recommendation
from utils.database import init_db, save_record, get_history

# Configure application layout
st.set_page_config(page_title="Tomato Crop Health Advisor", layout="wide")

# Initialize SQLite database
init_db()

# Sidebar: Sensor Inputs and Leaf Photo Upload
with st.sidebar:
    st.header("Crop Health Check")
    leaf_image = st.file_uploader("Upload Leaf Photo", type=["jpg", "jpeg", "png"])
    
    st.subheader("Field Conditions")
    soil_moisture = st.slider("Soil Moisture (%)", 0, 100, 35)
    temperature = st.number_input("Temperature (°C)", value=29.0)
    humidity = st.number_input("Humidity (%)", value=68.0)
    rainfall = st.number_input("Rainfall (mm)", value=0.0)
    
    analyze = st.button("Analyze Crop", type="primary")

st.title("Tomato Crop Health & Irrigation Advisor")

# Prediction Execution
if analyze:
    if leaf_image is not None:
        with st.spinner("Processing leaf diagnosis and irrigation requirement..."):
            # Step 1: Run CNN Disease Model
            disease, confidence = predict_disease(leaf_image)

            # Step 2: Run Random Forest Irrigation Model
            irrigation = predict_irrigation(soil_moisture, temperature, humidity, rainfall)

            # Step 3: Run Expert Recommendation Engine
            result = get_recommendation(disease, irrigation)

            # Step 4: Persist output to SQLite Database
            save_record(result['disease'], result['irrigation_need'], result['severity'])

        # Display Live Diagnostic Metrics
        col1, col2 = st.columns(2)
        with col1:
            st.image(leaf_image, caption="Uploaded Leaf Specimen", use_container_width=True)
            st.metric("Disease Detected", disease, f"{confidence * 100:.1f}% confidence")

        with col2:
            st.metric("Irrigation Need", irrigation)
            st.metric("Disease Severity", result['severity'])

        st.success(f"**Treatment Recommendation:** {result['treatment_advice']}")
        st.info(f"**Irrigation Advice:** {result['irrigation_advice']}")
    else:
        st.warning("Please upload a leaf photograph before running analysis.")
else:
    st.info("Upload a tomato leaf photograph and adjust field conditions in the sidebar, then click 'Analyze Crop'.")

# Section: Historical Logs from SQLite
st.markdown("---")
st.subheader("Recent Field Checks")

history_records = get_history(limit=10)
if history_records:
    history_df = pd.DataFrame(
        history_records,
        columns=["Date & Time", "Disease Detected", "Irrigation Need", "Severity"]
    )
    st.dataframe(history_df, use_container_width=True)
else:
    st.write("No diagnostic records logged yet.")