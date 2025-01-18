import pandas as pd
""" This file is unused for the data """
# Load the CSV file into a DataFrame
df = pd.read_csv('tmdb-scraper/output/all-movies-FINAL.csv')

# Columns to check for repetitions
columns_to_check = ['director', 'composer', 'writer', 'producer']

# Function to replace non-repeating values with 'other'
def replace_non_repeating(column):
    value_counts = column.value_counts()
    return column.apply(lambda x: x if value_counts.get(x, 0) > 1 else 'other')

# Apply the function to each specified column
for column in columns_to_check:
    if column in df.columns:
        df[column] = df[column].fillna('other')  # Fill NaN values with 'other'
        df[column] = replace_non_repeating(df[column])

# Save the modified DataFrame back to a CSV file
df.to_csv('tmdb-scraper/output/all-movies-FINAL-preprocess.csv', index=False)