import sys
from pathlib import Path
import pandas as pd

TRAIN_PATH=Path("/workspaces/ML/data/processed/train.csv")

EXPECTED_COLUMNS=["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)","target"]

def main() -> int:
    if not TRAIN_PATH.exists():
        print(f"Path {TRAIN_PATH} doesn not exist")
        return 1

    df=pd.read_csv(TRAIN_PATH)
    cols=list(df.columns)
    if cols!=EXPECTED_COLUMNS:
        print(f"Error: {TRAIN_PATH} doesn not contain expected columns")
        return 1

    null_counts=df.isnull().sum()
    if null_counts.any():
        print(f"Error: {TRAIN_PATH} contains null values")
        return 1
    
    print(f"[OK!] Validation successfull for {TRAIN_PATH}")
    return 0

if __name__=="__main__":
    sys.exit(main())