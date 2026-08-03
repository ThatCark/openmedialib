from media import models
class User:
    def __init__(self, username):
        self.__username = username
        self.__movie_collection =  []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        #if username not in used_usernames:
        self.__username = username

    def add_movie(self, movie):
        self.__movie_collection.append(movie)

    def delete_movie(self, movie):
        self.__movie_collection.remove(movie)
