import requests
import csv
import json
import os
from apikey import MY_API_KEY


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MY_API_KEY}"
}

# INPUT FILE NAME
with open('tmdb-scraper/output/all-movies-certif-final.csv', mode='r', newline='', encoding='utf-8') as top_rated_file:
    reader = csv.DictReader(top_rated_file)
    for row in reader:
        movie_id = row['id']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
        response = requests.get(url, headers=headers)
        data = response.json()
        # print(data)
        if 'posters' in data and len(data['posters']) > 0:
            poster_path = data['posters'][0]['file_path']
            poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"
            poster_response = requests.get(poster_url)
            if poster_response.status_code == 200:
                with open(f"tmdb-scraper/posters/{movie_id}.png", 'wb') as poster_file:
                    poster_file.write(poster_response.content)
                print(f"Saved poster for movie: {row['title']}")
            else:
                print(f"Failed to download poster for movie: {row['title']}")
        else:
            print(f"No poster available for movie: {row['title']}")
        # parents_rating = get_parents_rating(data)
        # # Write the data to the CSV file
        # with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     writer.writerow([row['title'], row['id'], row['release_date'], row['vote_average'], parents_rating, row['actors'], row['director'], row['composer'], row['writer'], row['producer'], row['budget'], row['genres'], row['runtime'], row['origin_country'], row['overview'], row['plot-vector']])
        # print(f"Processed movie: {row['title']}")
    print("Complete")