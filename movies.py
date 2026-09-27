movies = [
    "Avengers: Endgame",
    "3 Idiots",
    "Interstellar",
    "The Conjuring"
]


def show_movies():
    print()
    print("------ MOVIES AVAILABLE ------")

    for i in range(len(movies)):
        print(i + 1, ".", movies[i])


def get_movie(number):
    return movies[number - 1]