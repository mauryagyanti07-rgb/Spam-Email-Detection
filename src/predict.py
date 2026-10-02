import pickle
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.preprocessing import clean_text

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_PATH = MODELS_DIR / "spam_model.pkl"
VECTORIZER_PATH = MODELS_DIR / "tfidf_vectorizer.pkl"


def load_artifacts():
    if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
        raise FileNotFoundError("Model artifacts are missing. Train the model first.")

    with MODEL_PATH.open("rb") as model_file:
        model = pickle.load(model_file)

    with VECTORIZER_PATH.open("rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    return model, vectorizer


def predict_message(message: str):
    if not isinstance(message, str) or not message.strip():
        raise ValueError("Message text cannot be empty.")

    model, vectorizer = load_artifacts()
    cleaned_message = clean_text(message)
    transformed = vectorizer.transform([cleaned_message])
    prediction = model.predict(transformed)[0]
    probabilities = model.predict_proba(transformed)[0]

    label_index = list(model.classes_).index(prediction)
    confidence = float(probabilities[label_index])

    return {
        "prediction": prediction,
        "confidence": round(confidence, 4),
    }
