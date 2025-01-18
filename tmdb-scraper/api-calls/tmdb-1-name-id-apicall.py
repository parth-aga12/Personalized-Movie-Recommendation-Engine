import requests
import csv
import json
import os
from apikey import MY_API_KEY

# FILE NAME
csv_file = 'first_page_top_rated_movies.csv'
# Create CSV file and write headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'id'])

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MY_API_KEY}"
}
# https://developer.themoviedb.org/reference/movie-top-rated-list
for page in range(1, 2):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    response = requests.get(url, headers=headers)
    data = response.json()

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if 'results' in data:
            for movie in data['results']:
                writer.writerow([movie['title'], movie['id']])
        else:
            print(f"No results found for page {page}")
    print(page)

# TO GET MOVIE ID USING NAME:
# https://developer.themoviedb.org/reference/search-movie