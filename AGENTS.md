# AGENTS.md

## Project overview
This repository implements a spam-email detection API based on the PRD in `AIDOCS/PRD.md`.
The project follows a simple end-to-end NLP pipeline:

1. Load the SMS spam dataset from `data/SMSSpamCollection`
2. Validate and clean the text data
3. Train a TF-IDF + Logistic Regression model
4. Save model artifacts under `models/`
5. Serve predictions via Flask at `app.py`

## Project structure
- `app.py` — Flask API entry point
- `src/load_data.py` — dataset loading and validation utilities
- `src/preprocessing.py` — reusable text cleaning helpers
- `src/train.py` — model training and artifact saving
- `src/predict.py` — model loading and prediction utilities
- `data/SMSSpamCollection` — raw training data
- `models/` — serialized model and vectorizer files

## Commands
Run training:
```powershell
python src/train.py
```

Run the API:
```powershell
python app.py
```

Test the health endpoint:
```powershell
curl http://127.0.0.1:5000/
```

Test prediction:
```powershell
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"text\":\"Congratulations! You have won a free prize.\"}"
```

## Coding conventions
- Prefer reusable functions over inline logic.
- Keep preprocessing consistent between training and inference.
- Preserve the model and vectorizer artifact names used by the API.
- Do not log full customer message content in production.
- Keep the API responses JSON-based and consistent with the PRD.

## Memory guidance
- Do not move or rename the dataset without updating paths in code.
- Reuse the saved tf-idf vectorizer when creating predictions.
- If model files are missing, train the model before starting the API.
