# FUNCTION build_taste_profile_ml(user_ratings, public_ratings, movie_metadata):
#     """
#     Builds the taste profile using a machine learning approach.
#     Args:
#         user_ratings: List of movies the user has rated with ratings.
#         public_ratings: Dictionary of movies with public ratings.
#         movie_metadata: Metadata (genres, directors, cast) for all movies.
#     Returns:
#         taste_profile: Dictionary of predicted preference shifts for genres, directors, and cast.
#     """
#     dataset = []

#     # Prepare dataset for ML training
#     FOR movie IN user_ratings:
#         user_rating = movie["user_rating"]
#         public_rating = public_ratings[movie["title"]]["public_rating"]
#         difference = user_rating - public_rating

#         sample = {
#             "genres": movie_metadata[movie["title"]]["genres"],
#             "directors": movie_metadata[movie["title"]]["directors"],
#             "cast": movie_metadata[movie["title"]]["cast"],
#             "difference": difference
#         }
#         dataset.append(sample)

#     # Train regression model
#     X, y = PREPARE_FEATURES_AND_TARGET(dataset)
#     model = TRAIN_REGRESSION_MODEL(X, y)

#     # Predict preference shifts
#     taste_profile = {"genres": {}, "directors": {}, "cast": {}}
#     FOR attribute IN ["genres", "directors", "cast"]:
#         unique_values = GET_UNIQUE_VALUES(attribute, dataset)
#         FOR value IN unique_values:
#             synthetic_sample = CREATE_SYNTHETIC_SAMPLE(attribute=value)
#             taste_profile[attribute][value] = model.PREDICT(synthetic_sample)

#     RETURN taste_profile
