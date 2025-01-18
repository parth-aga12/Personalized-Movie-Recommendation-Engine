import json
import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
data = pd.read_csv("tmdb-scraper/output/all-movies-FINAL-preprocess.csv")
print('started reading csv')

# Load the mappings
mappings = {}
columns_to_map = ['director', 'composer', 'writer', 'producer']
for column in columns_to_map:
    with open(f'tmdb-scraper/output/{column}_mapping.json', 'r') as f:
        mappings[column] = json.load(f)

# Function to encode a column using the mapping
def encode_column(column, mapping):
    encoded = np.zeros((data.shape[0], len(mapping)), dtype=int)
    for i, value in enumerate(data[column]):
        if value in mapping:
            encoded[i, mapping[value]] = 1
    return encoded.tolist()

# Encode each specified column and add as a new column in the DataFrame
for column in columns_to_map:
    if column in data.columns:
        encoded = encode_column(column, mappings[column])
        data[f"{column}_encoded"] = encoded

# Save the result to a new CSV file
data.to_csv("tmdb-scraper/output/movies_with_crew_encoding.csv", index=False)

print("One-hot encoding saved to movies_with_crew_encoding.csv")