import pandas as pd
""" Find average rating per person on crew: director, composer, writer and producer and create an entry per movie"""
# Load the CSV file into a DataFrame
data = pd.read_csv("tmdb-scraper/output/movies_with_genre_encoding.csv")

# Columns to calculate average ratings for
crew_columns = ['director', 'composer', 'writer', 'producer']

# Initialize dictionaries to store average ratings
average_ratings = {column: {} for column in crew_columns}

# Calculate the average rating for each crew member
for column in crew_columns:
    if column in data.columns:
        crew_ratings = data.groupby(column)['vote_average'].mean()
        average_ratings[column] = crew_ratings.to_dict()

# Function to get the average rating for a crew member
def get_average_rating(row, column):
    crew_member = row[column]
    return average_ratings[column].get(crew_member, None)

# Create new columns for average ratings
for column in crew_columns:
    data[f'{column}_avg_rating'] = data.apply(lambda row: get_average_rating(row, column), axis=1)

# Save the result to a new CSV file
data.to_csv("tmdb-scraper/output/movies_with_average_crew_ratings.csv", index=False)

print("Average crew ratings added and saved to movies_with_average_crew_ratings.csv")