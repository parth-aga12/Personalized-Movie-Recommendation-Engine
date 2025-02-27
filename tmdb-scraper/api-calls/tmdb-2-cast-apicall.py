import requests
import csv
import json
import os

# INPUT FILE NAME
csv_file = 'first-page-movie-details.csv'
# Create CSV file and write headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'id', 'actors', 'director', 'composer', 'writer', 'producer'])

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNTI0N2UzMGVkMWE0NzExZDAxNmU3MmEzNTUyYTQ4YyIsIm5iZiI6MTczNjAxNjIxNS4zODIwMDAyLCJzdWIiOiI2Nzc5ODE1NzgzMGE4ZjRjYzc2Njk1N2MiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.aryLHuME0O2JL-rfAPnjivV9BsEn6eVi15bSsxHTnCg"
}
# https://developer.themoviedb.org/reference/movie-credits
# OUTPUT FILE NAME
with open('first_page_top_rated_movies.csv', mode='r', newline='', encoding='utf-8') as top_rated_file:
    reader = csv.DictReader(top_rated_file)
    for row in reader:
        movie_id = row['id']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract the first 3 acting credits
        actors = [member['name'] for member in data['cast'][:3]]

        # Extract specific crew members
        director = next((member['name'] for member in data['crew'] if member['job'] == 'Director'), None)
        composer = next((member['name'] for member in data['crew'] if member['job'] == 'Original Music Composer'), None)
        screenplay = next((member['name'] for member in data['crew'] if member['job'] == 'Screenplay'), None)
        producer = next((member['name'] for member in data['crew'] if member['job'] == 'Producer'), None)

        # Write the data to the CSV file
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([row['title'], movie_id, actors, director, composer, screenplay, producer])
        print(f"Processed movie: {row['title']}")



