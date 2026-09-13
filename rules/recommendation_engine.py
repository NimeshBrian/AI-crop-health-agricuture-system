DISEASE_TREATMENTS = {
    "Bacterial_spot": "Apply copper-based bactericide spray. Remove and destroy infected leaves.",
    "Early_blight": "Apply fungicide (chlorothalonil or copper-based). Remove lower infected leaves.",
    "Late_blight": "Apply fungicide immediately — spreads fast. Remove severely infected plants.",
    "Yellow_Leaf_Curl_Virus": "Remove and destroy infected plants. Control whitefly population.",
    "Healthy": "No treatment needed. Continue regular monitoring."
}

IRRIGATION_ADVICE = {
    "Low": "Soil moisture is sufficient. No immediate irrigation needed.",
    "Medium": "Irrigate within the next 1-2 days.",
    "High": "Irrigate today — soil moisture is critically low."
}

def get_recommendation(disease, irrigation_need):
    treatment = DISEASE_TREATMENTS.get(disease, "Unknown disease — consult an expert.")
    irrigation = IRRIGATION_ADVICE.get(irrigation_need, "Unknown irrigation level.")

    if disease != "Healthy" and irrigation_need == "High":
        severity = "Critical"
    elif disease != "Healthy" or irrigation_need == "High":
        severity = "Moderate"
    else:
        severity = "Low"

    return {
        "disease": disease,
        "irrigation_need": irrigation_need,
        "severity": severity,
        "treatment_advice": treatment,
        "irrigation_advice": irrigation
    }

if __name__ == "__main__":
    print(get_recommendation("Late_blight", "High"))