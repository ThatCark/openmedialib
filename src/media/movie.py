from media import Media

class Movie(Media):
    def __init__(self, creator, release):
        self.__creator = creator
        self.__release = release
        
    @property
    def creator(self):
        return self.__creator

    @property
    def release(self):
        return self.__release

    def to_dict(self):
        return {
            "type" : "Movie",
            "creator" : self.__creator,
            "release" : self.__release
        }