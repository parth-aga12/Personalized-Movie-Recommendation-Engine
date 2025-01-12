import pandas as pd
import json
import spacy
import os
import csv
# Load the spaCy model
nlp = spacy.load('en_core_web_lg')


# INPUT FILE NAME
csv_file = 'tmdb-scraper/all-movies-vectors-final.csv'
# Create CSV file and write headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'id', 'release_date', 'vote_average', 'actors', 'director', 'composer', 'writer', 'producer', 'budget', 'genres', 'runtime', 'origin_country', 'overview', 'plot-vector'])

# Function to get the vector of the plot
def get_plot_vector(plot):
    doc = nlp(plot)
    vector_array = doc.vector
    vector_list = vector_array.tolist()
    # vector_array = list(map(int, vector_list))
    return vector_list

with open('tmdb-scraper/all-movies-details-final.csv', mode='r', newline='', encoding='utf-8') as top_rated_file:
    reader = csv.DictReader(top_rated_file)
    for row in reader:
        # Write the data to the CSV file
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            budget = row.get('budget', None)
            genres = row.get('genres', None)
            runtime = row.get('runtime', None)
            origin_country = row.get('origin_country', None)
            overview = row.get('overview', None)
            plot_vector = get_plot_vector(overview) if overview else None
            writer.writerow([row['title'], row['id'], row['release_date'], row['vote_average'], row['actors'], row['director'], row['composer'], row['writer'], row['producer'], budget, genres, runtime, origin_country, overview, plot_vector])
        # print(f"Processed movie: {row['title']}")
    print("Complete")



# # Apply the function to the plot column and create a new column for the vectors
# df['plot_vector'] = df['overview'].apply(get_plot_vector)

# # Drop the original plot column
# df = df.drop(columns=['overview'])

# # Save the new DataFrame to a new CSV file
# df.to_csv('all-movie-details-with-vectors.csv', index=False)