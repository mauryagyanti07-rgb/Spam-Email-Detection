import pickle
import sys
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.preprocessing import clean_text

DATASET_PATH = Path(__file__).resolve().parent.parent / "data" / "SMSSpamCollection"
MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_PATH = MODELS_DIR / "spam_model.pkl"
VECTORIZER_PATH = MODELS_DIR / "tfidf_vectorizer.pkl"


def load_dataset(path: Path = DATASET_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, sep="\t", header=None, names=["label", "text"])
    df = df.copy()

    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df["text"] = df["text"].fillna("").astype(str).str.strip()

    if df.empty:
        raise ValueError("Dataset is empty.")

    df["text"] = df["text"].apply(clean_text)
    df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)

    valid_labels = {"ham", "spam"}
    invalid = set(df["label"]) - valid_labels
    if invalid:
        raise ValueError(f"Dataset contains invalid labels: {sorted(invalid)}")

    return df


def train_model() -> dict:
    MODELS_DIR.mkdir(exist_ok=True)
    df = load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label"],
        test_size=0.2,
        random_state=42,
        stratify=df["label"],
    )

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_tfidf, y_train)

    predictions = model.predict(X_test_tfidf)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, pos_label="spam", zero_division=0),
        "recall": recall_score(y_test, predictions, pos_label="spam", zero_division=0),
        "f1": f1_score(y_test, predictions, pos_label="spam", zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, predictions, labels=["ham", "spam"]).tolist(),
    }

    with MODEL_PATH.open("wb") as model_file:
        pickle.dump(model, model_file)

    with VECTORIZER_PATH.open("wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    return metrics


if __name__ == "__main__":
    metrics = train_model()
    print("Training complete")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1-score: {metrics['f1']:.4f}")
    print(f"Confusion Matrix: {metrics['confusion_matrix']}")
