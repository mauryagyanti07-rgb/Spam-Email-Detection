# Spam Email Detection

A Flask-based spam detection API that uses a text classification pipeline built around the UCI SMS Spam Collection dataset.

## Features
- Dataset loading and validation
- Text preprocessing and normalization
- TF-IDF feature extraction
- Logistic Regression classification baseline
- Model artifact persistence
- REST API for prediction

## Repository structure
```text
Spam-Email-Detection/
├── AIDOCS/
│   └── PRD.md
├── data/
│   └── SMSSpamCollection
├── models/
├── src/
│   ├── __init__.py
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
├── AGENTS.md
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Train the model
```powershell
python src/train.py
```

## Run the API
```powershell
python app.py
```

## Example API call
```powershell
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"text\":\"Congratulations! You have won a free prize.\"}"
```

Response example:
```json
{
  "prediction": "spam",
  "confidence": 0.95
}
```

## Notes
This project follows the requirements described in the PRD and emphasizes a clean, GitHub-friendly structure for a portfolio-ready ML API.
