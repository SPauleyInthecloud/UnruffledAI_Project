import os
import pickle
import numpy as np
import tensorflow as tf
from django.conf import settings

# ---------------------------------------------------
# MODEL FILE PATHS
# ---------------------------------------------------
MODEL_DIR = os.path.join(settings.BASE_DIR, "core", "model_files")
MODEL_PATH = os.path.join(MODEL_DIR, "burnout_model.keras")

SCALER_PATH = os.path.join(MODEL_DIR, "burnout_scaler.pkl")
CLASS_ENCODER_PATH = os.path.join(MODEL_DIR, "burnout_class_encoder.pkl")
PLANET_ENCODER_PATH = os.path.join(MODEL_DIR, "burnout_planet_encoder.pkl")
HOUSE_ENCODER_PATH = os.path.join(MODEL_DIR, "burnout_house_encoder.pkl")
SLEEP_ENCODER_PATH = os.path.join(MODEL_DIR, "burnout_sleep_encoder.pkl")


# ---------------------------------------------------
# GLOBAL PLACEHOLDERS
# These stay empty until prediction is actually needed.
# This prevents Django / GitHub Actions from loading TensorFlow
# during startup checks.
# ---------------------------------------------------
burnout_model = None
scaler = None
class_encoder = None
planet_encoder = None
house_encoder = None
sleep_encoder = None


# ---------------------------------------------------
# LAZY LOAD MODEL + ENCODERS
# ---------------------------------------------------
def load_burnout_assets():
    """
    Loads the TensorFlow model, scaler, and encoders only when needed.
    This makes the app safer for GitHub Actions, Docker, and AWS deployment.
    """
    global burnout_model
    global scaler
    global class_encoder
    global planet_encoder
    global house_encoder
    global sleep_encoder

    if burnout_model is None:
        burnout_model = tf.keras.models.load_model(MODEL_PATH)

    if scaler is None:
        with open(SCALER_PATH, "rb") as f:
            scaler = pickle.load(f)

    if class_encoder is None:
        with open(CLASS_ENCODER_PATH, "rb") as f:
            class_encoder = pickle.load(f)

    if planet_encoder is None:
        with open(PLANET_ENCODER_PATH, "rb") as f:
            planet_encoder = pickle.load(f)

    if house_encoder is None:
        with open(HOUSE_ENCODER_PATH, "rb") as f:
            house_encoder = pickle.load(f)

    if sleep_encoder is None:
        with open(SLEEP_ENCODER_PATH, "rb") as f:
            sleep_encoder = pickle.load(f)


# ---------------------------------------------------
# PREDICT BURNOUT
# ---------------------------------------------------
def predict_burnout(
    heart_rate,
    hrv_score,
    sleep_hours,
    activity_level,
    stress_level,
    transit_planet,
    natal_house,
    sleep_quality
):
    """
    Returns burnout category and numeric burnout risk score.

    Example return:
    ("medium", 0.58)
    """

    # Load model/scaler/encoders only when this function runs
    load_burnout_assets()

    # Encode categorical values
    planet_val = planet_encoder.transform([transit_planet])[0]
    house_val = house_encoder.transform([natal_house])[0]
    sleep_val = sleep_encoder.transform([sleep_quality])[0]

    # Build feature array
    features = np.array([[
        heart_rate,
        hrv_score,
        sleep_hours,
        activity_level,
        stress_level,
        planet_val,
        house_val,
        sleep_val
    ]])

    # Scale inputs
    features_scaled = scaler.transform(features)

    # Run model prediction
    class_pred, score_pred = burnout_model.predict(features_scaled)

    # Convert class prediction into label
    class_idx = np.argmax(class_pred, axis=1)[0]
    burnout_category = class_encoder.inverse_transform([class_idx])[0]

    # Convert score output into float
    burnout_score = float(score_pred[0][0])

    return burnout_category, burnout_score