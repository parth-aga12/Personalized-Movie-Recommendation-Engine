import requests
import csv
import json
import os
from apikey import MY_API_KEY

# INPUT FILE NAME
csv_file = 'first_page_movie-details-final.csv'
# Create CSV file and write headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'id', 'release_date', 'vote_average', 'actors', 'director', 'composer', 'writer', 'producer', 'budget', 'genres', 'runtime', 'origin_country', 'overview'])

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MY_API_KEY}"
}
# https://developer.themoviedb.org/reference/movie-details
# OUTPUT FILE NAME
with open('first-page-movie-details.csv', mode='r', newline='', encoding='utf-8') as top_rated_file:
    reader = csv.DictReader(top_rated_file)
    for row in reader:
        movie_id = row['id']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()
        # Extract budget, genres, runtime, and origin country
        budget = data.get('budget', None)
        genres = [genre['name'] for genre in data.get('genres', [])]
        runtime = data.get('runtime', None)
        origin_country = data.get('origin_country', None)
        overview = data.get('overview', None)
        release_date = data.get('release_date', None)
        vote_average = data.get('vote_average', None)
        # Write the data to the CSV file
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([row['title'], movie_id, release_date, vote_average, row['actors'], row['director'], row['composer'], row['writer'], row['producer'], budget, genres, runtime, origin_country, overview])
        print(f"Processed movie: {row['title']}")



