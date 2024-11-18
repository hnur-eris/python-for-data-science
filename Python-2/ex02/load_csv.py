import pandas as pd


def load(path: str):
    """
        Loads a CSV file and returns it as a DataFrame.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimension {dataset.shape}")
        return dataset
    except (FileNotFoundError,
            pd.errors.EmptyDataError,
            pd.errors.ParserError) as e:
        print(f"File not found: {e}")
        return None
