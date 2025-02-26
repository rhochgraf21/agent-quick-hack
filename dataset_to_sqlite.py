import pandas as pd
from datasets import load_dataset
import sqlite3

dataset_name = "HathawayLiu/housing_dataset"
# For loading the dataset from hugging face
ds = load_dataset(dataset_name)
print(f"Loaded dataset: {dataset_name}" )

df = pd.concat([ds['train'].to_pandas(), ds['test'].to_pandas()])



db_filename = f"housing_data.sqlite"



# Connect to SQLite and save DataFrame
conn = sqlite3.connect(db_filename)
df.to_sql("housing_data", conn, index=False, if_exists="replace")
conn.close()

print(f"Saved dataset as {db_filename}")