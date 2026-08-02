from media import Media

class Movie(Media):
    def __init__(self, owner, creator, release):
        self.__owner = owner
        self.__creator = creator
        self.__release

    @property
    def owner(self):
        return self.__owner

    @property
    def creator(self):
        return self.__creator

    @property
    def release(self):
        return self.__creator