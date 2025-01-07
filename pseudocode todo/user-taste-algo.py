# FUNCTION build_taste_profile(user_ratings, public_ratings, movie_metadata):
#     """
#     Builds the taste profile using an algorithmic approach.
#     Args:
#         user_ratings: List of movies the user has rated with ratings.
#         public_ratings: Dictionary of movies with public ratings.
#         movie_metadata: Metadata (genres, directors, cast) for all movies.
#     Returns:
#         taste_profile: Dictionary of preference shifts for genres, directors, and cast.
#     """
#     taste_profile = {"genres": {}, "directors": {}, "cast": {}}
#     attribute_counts = {"genres": {}, "directors": {}, "cast": {}}

#     FOR movie IN user_ratings:
#         user_rating = movie["user_rating"]
#         public_rating = public_ratings[movie["title"]]["public_rating"]
#         difference = user_rating - public_rating

#         # Update shifts for each attribute
#         FOR attribute IN ["genres", "directors", "cast"]:
#             FOR value IN movie_metadata[movie["title"]][attribute]:
#                 IF value NOT IN taste_profile[attribute]:
#                     taste_profile[attribute][value] = 0
#                     attribute_counts[attribute][value] = 0

#                 taste_profile[attribute][value] += difference
#                 attribute_counts[attribute][value] += 1

#     # Normalize shifts
#     FOR attribute IN ["genres", "directors", "cast"]:
#         FOR value IN taste_profile[attribute]:
#             taste_profile[attribute][value] /= attribute_counts[attribute][value]

#     RETURN taste_profile
