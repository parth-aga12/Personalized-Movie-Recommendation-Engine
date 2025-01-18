from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
import ast

try:
    # Load the CSV file into a DataFrame
    data = pd.read_csv("tmdb-scraper/output/all-movies-FINAL.csv")

    # Convert genres from string representation of list to actual Python list
    data['genres'] = data['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

    # Use MultiLabelBinarizer to generate one-hot encoding for genres
    mlb = MultiLabelBinarizer()
    genre_one_hot = mlb.fit_transform(data['genres'])

    # Convert the one-hot encoding into a list of arrays
    data['genre_one_hot'] = [list(map(int, row)) for row in genre_one_hot]

    # Create a new DataFrame with all original columns and genre_one_hot
    output_data = data.copy()
    output_data['genre_one_hot'] = data['genre_one_hot']

    # Save the result to a new CSV file
    output_data.to_csv("tmdb-scraper/output/movies_with_genre-encoding.csv", index=False)

    print("One-hot encoding saved to movies_with_all_encoding.csv")

except Exception as e:
    print(f"An error occurred: {e}")