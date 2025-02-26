import pandas as pd
from datasets import load_dataset
import sqlite3

dataset_name = "HathawayLiu/housing_dataset"
# For loading the dataset from hugging face
ds = load_dataset(dataset_name)
print(f"Loaded dataset: {dataset_name}" )

for split in ds.keys():
    # Convert dataset to pandas DataFrame
    df = ds[split].to_pandas()
    print(f"converted {split} to pandas DataFrame")

    db_filename = f"db_{split}.sqlite"

    # Connect to SQLite and save DataFrame
    conn = sqlite3.connect(db_filename)
    df.to_sql(split, conn, index=False, if_exists="replace")
    conn.close()

    print(f"Saved {split} dataset as {db_filename}")