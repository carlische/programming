from movies1 import MovieRecommender, movies_file, histories_file

def main():
    """
    Основная функция для MovieRecommender.
    """
    recommender = MovieRecommender(movies_file=movies_file, histories_file=histories_file)

    user_input = input("Введите список идентификаторов просмотренных фильмов, разделенных запятыми:\n")
    try:
        user_movies_list = [int(movie_id_str.strip()) for movie_id_str in user_input.split(',') if movie_id_str.strip().isdigit()]
    except ValueError:
        print("Некорректный ввод. Убедитесь, что вы вводите только целые числа, разделенные запятыми.")
        user_movies_list = []

    recommendation = recommender.recommend(user_movies_list)

    if recommendation:
        print(recommendation)
    else:
        print("Нет доступных рекомендаций.")

if __name__ == "__main__":
    main()