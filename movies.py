"""
Author: Andrew
Program to process and display movie information from a file.
"""

def get_movies(filename):
    """Reads movie information from a file and returns a list of tuples with each movie's details."""
    movies = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            title, genre, year, runtime = line.strip().split(',')
            movies.append((title, genre, int(year), int(runtime)))
    return movies

def list_movies(movies):
    """Displays movie information in a formatted table, showing the first 25 characters of the title."""
    print(f"{'Title':<25} {'Genre':<10} {'Year':<5} {'Runtime'}")
    print("-" * 50)
    for title, genre, year, runtime in movies:
        print(f"{title[:25]:<25} {genre:<10} {year:<5} {runtime}")

def get_longest_movie(movies):
    """Returns the title and runtime of the longest movie."""
    longest_movie = movies[0]  # Start by assuming the first movie is the longest
    for movie in movies:
        if movie[3] > longest_movie[3]:  # Compare runtime
            longest_movie = movie
    return longest_movie[0], longest_movie[3]

def get_genres(movies):
    genre_movies = []
    for movie in movies:
        if movie [1] not in genre_movies:
            genre_movies.append(movie [1])

    return genre_movies



def main():
    movies = get_movies("movies.txt")

    print("All Movies:")
    list_movies(movies)

    print()
    title, longest = get_longest_movie(movies)
    print("The longest movie is:", title)
    print("Runtime is", longest, "minutes")
    print("The genre is:", get_genres(movies))

main()