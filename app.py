import sys
from pathlib import Path

from flask import Flask, jsonify, request

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.predict import predict_message

app = Flask(__name__)


@app.get("/")
def health_check():
    return jsonify({"message": "Spam Detection API is running"})


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True)

    if payload is None:
        return jsonify({"error": "Request body must be valid JSON."}), 400

    text = payload.get("text")

    if text is None:
        return jsonify({"error": "Message text is required."}), 400

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Message text cannot be empty."}), 400

    try:
        result = predict_message(text)
        return jsonify(result), 200
    except FileNotFoundError:
        return jsonify({
            "error": "Model is not available. Please train the model first."
        }), 500
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)