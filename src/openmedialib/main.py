# from lending import Lending
from media.movie import Movie
from user.user import User
from lending.lending import Lending
from memory.jsonConnector import JSONConnector

#First step: build cli-tool (change to gui later)
test_username = input ("Bitte Namen eingeben: ")
test_user = User(test_username)
user_input = 0
conn = JSONConnector(test_username)
#change interaction for handling generic media types instead of only handling movies
test_user.__movie_collection = conn.load()

while user_input != 5:
    print("Please choose an option:")
    print("(1) Add a movie")
    print("(2) Lend a movie")
    print("(3) Show your movie library")
    print("(4) Show your lendings")
    #what about movies you have borrowed?
    print("(5) Quit")

    user_input = input("User input: ")
    if user_input == 1:
        title = input("Input movie title: ")
        creator = input("Input movie creator: ") #automate getting this data from api later
        release = input("Input movie release: ") #automate getting this data from api later
        test_user.add_movie(Movie(title, creator, release))
    elif user_input == 2:
        borrower = input("Who borrowed your movie? ")
        movie = input("Which movie have you lend?")
        new_lending = Lending(test_user, borrower, movie)
        #Add constructor call for movie

        # to catch:
        # 1. movie is already lend 
        # 2. user doesnt own the movie 
    elif user_input == 3:
        for movie_num, movie in enumerate(test_user.__movie_collection):
            print(f"Movie number {movie_num}:")
            print(f"Title: {movie.title}")
            print(f"Director: {movie.creator}")
            print(f"Release: {movie.release}")
    elif user_input == 4:
        print("not implemented yet")
    elif user_input == 5: 
        conn.save(test_user.__movie_collection)
        conn.close()

        print("Good bye!")
    else:
        print("Unknown command. Please try again.")

        

    # user_input = input("Please ")
