movies_file = 'movies1.txt'
histories_file = 'histories1.txt'

class MovieRecommender:

    def __init__(self, movies_file=None, histories_file=None, movies=None, histories=None):
        """Инициализирует класс, загружает данные о фильмах и истории просмотров."""
        if movies:
            self.movies = movies
        else:
            self.movies_file = movies_file
            self.movies = dict()
            self.load_movies()
        if histories:
            self.histories = histories
        else:
            self.histories_file = histories_file
            self.histories = list()
            self.load_histories()

    def load_movies(self):
        """Загружает список фильмов из файла."""
        try:
            with open(self.movies_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        movie_id_str, movie_name = line.split(',', 1)
                        movie_id = int(movie_id_str)
                        self.movies[movie_id] = movie_name
        except FileNotFoundError:
            print(f"Файл {self.movies_file} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке списка фильмов: {e}")


    def load_histories(self):
        """Загружает историю просмотров пользователей из файла."""
        try:
            with open(self.histories_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        movie_ids = [int(movie_id_str) for movie_id_str in line.split(',')]
                        self.histories.append(movie_ids)
        except FileNotFoundError:
            print(f"Файл {self.histories_file} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке истории просмотров: {e}")

    def recommend(self, user_movies_list):
        """
        Рекомендует фильм на основе истории просмотров пользователя.
        """
        if not isinstance(user_movies_list, list) or not all(isinstance(mid, int) for mid in user_movies_list):
            raise ValueError("Список фильмов должен быть списком целых чисел.")

        if not user_movies_list:
            return None

        user_movies_set = set(user_movies_list)
        matching_histories = list()

        for history in self.histories:
            history_set = set(history)
            common_movies = user_movies_set.intersection(history_set)
            overlap_ratio = len(common_movies) / len(user_movies_set)
            if overlap_ratio >= 0.5:
                matching_histories.append((history, overlap_ratio))

        recommended_movies = dict()
        for history, weight in matching_histories:
            for movie_id in history:
                if movie_id not in user_movies_set:
                    if movie_id in recommended_movies:
                        recommended_movies[movie_id] += weight
                    else:
                        recommended_movies[movie_id] = weight

        if not recommended_movies:
            return None

        max_weight = max(recommended_movies.values())
        top_movies = [movie_id for movie_id, weight in recommended_movies.items() if weight == max_weight]

        recommended_movie_id = top_movies[0]
        return self.movies.get(recommended_movie_id, None)