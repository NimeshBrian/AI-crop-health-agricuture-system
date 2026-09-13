# Disease treatment and irrigation rule-based recommendation logic

TREATMENTS = {
    "Tomato___Bacterial_spot": "Apply copper-based bactericides. Avoid overhead watering to reduce splash transmission.",
    "Tomato___Early_blight": "Apply fungicides containing chlorothalonil or mancozeb. Remove infected lower leaves.",
    "Tomato___Late_blight": "Apply metalaxyl or copper-based fungicides immediately. Remove severely damaged plants.",
    "Tomato___Leaf_Mold": "Improve air circulation in the greenhouse and avoid high relative humidity.",
    "Tomato___Septoria_leaf_spot": "Remove lower affected leaves. Apply protective fungicides and mulch the soil.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Use insecticidal soap or neem oil spray. Keep foliage clean.",
    "Tomato___Target_Spot": "Ensure proper spacing for air flow. Apply recommended protective fungicides.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Control whitefly vectors using sticky traps and insecticides. Remove infected hosts.",
    "Tomato___Tomato_mosaic_virus": "Sanitize tools with trisodium phosphate. Discard infected plants immediately.",
    "Tomato___healthy": "Plant is healthy. Continue regular monitoring and balanced fertilization."
}

def get_recommendation(disease_name, irrigation_need):
    """
    Combines disease prediction and irrigation requirement to generate advisory actions.
    """
    # Determine severity based on disease condition
    if "healthy" in disease_name.lower():
        severity = "None"
    elif any(severe in disease_name.lower() for severe in ["late_blight", "virus"]):
        severity = "High"
    else:
        severity = "Moderate"

    # Fetch treatment advice
    treatment = TREATMENTS.get(disease_name, "Consult an agricultural officer for localized advice.")

    # Tailor irrigation advisory
    if irrigation_need == "High":
        irrigation_advice = "Irrigate the field immediately. Deliver water directly to the soil roots, avoiding wetting leaves."
    elif irrigation_need == "Medium":
        irrigation_advice = "Soil moisture is acceptable. Schedule standard drip irrigation during morning hours."
    else:
        irrigation_advice = "Sufficient soil moisture detected. Postpone irrigation to avoid root fungal infection."

    return {
        "disease": disease_name,
        "irrigation_need": irrigation_need,
        "severity": severity,
        "treatment_advice": treatment,
        "irrigation_advice": irrigation_advice
    }