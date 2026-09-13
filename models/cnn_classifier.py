import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from PIL import Image
import numpy as np

# Load trained MobileNetV2 model
MODEL_PATH = 'models/saved/tomato_disease_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Class order matches training indices exactly
CLASS_NAMES = [
    "Bacterial_spot",
    "Early_blight",
    "Late_blight",
    "Yellow_Leaf_Curl_Virus",
    "Healthy"
]

def predict_disease(image_file):
    """
    Takes an image file/path, preprocesses it, and returns
    the predicted disease class name and prediction confidence.
    """
    img = Image.open(image_file).convert('RGB').resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    
    predictions = model.predict(img_array)
    idx = np.argmax(predictions[0])
    confidence = float(predictions[0][idx])
    
    return CLASS_NAMES[idx], confidence

if __name__ == "__main__":
    print("CNN Classifier wrapper is loaded and ready.")