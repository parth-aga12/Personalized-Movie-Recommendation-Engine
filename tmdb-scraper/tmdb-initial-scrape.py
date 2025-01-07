import requests
import csv
import json
import os
from apikey import MY_API_KEY

csv_file = 'top_rated_movies.csv'
# Create CSV file and write headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'id', 'release_date', 'vote_average'])

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MY_API_KEY}"
}

for page in range(501, 502):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    response = requests.get(url, headers=headers)
    data = response.json()

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if 'results' in data:
            for movie in data['results']:
                writer.writerow([movie['title'], movie['id'], movie['release_date'], movie['vote_average']])
        else:
            print(f"No results found for page {page}")
    print(page)



# url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNTI0N2UzMGVkMWE0NzExZDAxNmU3MmEzNTUyYTQ4YyIsIm5iZiI6MTczNjAxNjIxNS4zODIwMDAyLCJzdWIiOiI2Nzc5ODE1NzgzMGE4ZjRjYzc2Njk1N2MiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.aryLHuME0O2JL-rfAPnjivV9BsEn6eVi15bSsxHTnCg"
# }

# response = requests.get(url, headers=headers)

# print(response.text)