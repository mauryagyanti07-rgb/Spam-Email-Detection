from pathlib import Path

import pandas as pd


DATASET_PATH = Path(__file__).resolve().parent.parent / "data" / "SMSSpamCollection"


def load_dataset(path: str | Path = DATASET_PATH) -> pd.DataFrame:
    """Load and validate the raw SMS spam dataset."""
    dataset_path = Path(path)
    df = pd.read_csv(dataset_path, sep="\t", header=None, names=["label", "text"])

    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("Dtypes:\n", df.dtypes)
    print("Missing values:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())
    print("Label distribution:\n", df["label"].value_counts())
    print("Sample:\n", df.head())

    df["text"] = df["text"].fillna("").astype(str).str.lower().str.strip()
    print("Normalized sample:\n", df.head())
    return df


if __name__ == "__main__":
    load_dataset()
