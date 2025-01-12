import requests
import csv
import json
import os
from apikey import MY_API_KEY

def get_parents_rating(data):
    release_dates_data = data.get("release_dates", {}).get("results", [])
    for country_data in release_dates_data:
        for release_date in country_data.get("release_dates", []):
            certification = release_date.get("certification", "").strip()
            if certification.isdigit():  # Check if the certification is an integer-only string
                parents_rating = int(certification)  # Convert to integer and return
                return parents_rating

# OUTPUT FILE NAME
csv_file = 'tmdb-scraper/output/all-movies-certif-final.csv'
# Create CSV file and write headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'id', 'release_date', 'vote_average', 'parents_rating', 'actors', 'director', 'composer', 'writer', 'producer', 'budget', 'genres', 'runtime', 'origin_country', 'overview', 'plot-vector'])

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MY_API_KEY}"
}
# INPUT FILE NAME
with open('tmdb-scraper/output/all-movies-vectors-final.csv', mode='r', newline='', encoding='utf-8') as top_rated_file:
    reader = csv.DictReader(top_rated_file)
    for row in reader:
        movie_id = row['id']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?append_to_response=release_dates&language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()
        parents_rating = get_parents_rating(data)
        # Write the data to the CSV file
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([row['title'], row['id'], row['release_date'], row['vote_average'], parents_rating, row['actors'], row['director'], row['composer'], row['writer'], row['producer'], row['budget'], row['genres'], row['runtime'], row['origin_country'], row['overview'], row['plot-vector']])
        # print(f"Processed movie: {row['title']}")
    print("Complete")



# url = f"https://api.themoviedb.org/3/movie/%7Bmovie_ID%7D?language=en-US&append_to_response=release_dates"
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print(f"Error: API request failed with status code {response.status_code}")
#     print(f"Response: {response.text}")
#     return None

# data = response.json()

# release_dates_data = data.get("release_dates", {}).get("results", [])
# for country_data in release_dates_data:
#     for release_date in country_data.get("release_dates", []):
#         certification = release_date.get("certification", "").strip()
#         if certification.isdigit():  # Check if the certification is an integer-only string
#             parents_rating = int(certification)  # Convert to integer and return