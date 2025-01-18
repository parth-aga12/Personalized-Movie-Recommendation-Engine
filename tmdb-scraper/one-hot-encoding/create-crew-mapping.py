import pandas as pd
import json

# Load the CSV file into a DataFrame
df = pd.read_csv('tmdb-scraper/output/all-movies-FINAL-preprocess.csv')

# Columns to create mappings for
columns_to_map = ['director', 'composer', 'writer', 'producer']

# Dictionary to store mappings
mappings = {}

# Create mappings for each specified column
for column in columns_to_map:
    if column in df.columns:
        # Create mapping for the column
        unique_values = df[column].unique()
        mapping = {value: idx for idx, value in enumerate(unique_values)}
        mappings[column] = mapping

# Save the mappings to separate JSON files
for column, mapping in mappings.items():
    with open(f'tmdb-scraper/output/{column}_mapping.json', 'w') as f:
        json.dump(mapping, f)

print("Mappings have been created and saved to JSON files.")