import unittest
from src.lab4.movies1 import MovieRecommender

class TestMovieRecommender(unittest.TestCase):

    def setUp(self):
        self.movies = {
            1: 'Мстители: Финал',
            2: 'Хатико',
            3: 'Дюна',
            4: 'Унесенные призраками'
        }
        self.histories = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        self.recommender = MovieRecommender(movies=self.movies, histories=self.histories)

    def test_recommendation(self):
        user_movies = [2, 4]
        recommended_movie = self.recommender.recommend(user_movies)
        self.assertEqual(recommended_movie, 'Дюна')

    def test_no_recommendation(self):
        user_movies = [1, 2, 3, 4]
        recommended_movie = self.recommender.recommend(user_movies)
        self.assertIsNone(recommended_movie)

    def test_edge_case_half_movies(self):
        user_movies = [1, 2]
        recommended_movie = self.recommender.recommend(user_movies)
        self.assertEqual(recommended_movie, 'Дюна')

    def test_error_handling_invalid_input(self):
        user_movies = ['a', None, 5]
        with self.assertRaises(ValueError):
            self.recommender.recommend(user_movies)

    def test_empty_user_movies(self):
        user_movies = list()
        recommended_movie = self.recommender.recommend(user_movies)
        self.assertIsNone(recommended_movie)

    def test_recommendation_with_weights(self):
        user_movies = [1, 3]
        recommended_movie = self.recommender.recommend(user_movies)
        self.assertEqual(recommended_movie, 'Хатико')

if __name__ == '__main__':
    unittest.main()