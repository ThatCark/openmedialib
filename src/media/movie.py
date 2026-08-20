from media import Media

class Movie(Media):
    def __init__(self, title, creator, release):
        self.__creator = creator
        self.__release = release
        self.__title = title

    @property
    def creator(self):
        return self.__creator

    @property
    def release(self):
        return self.__release

    @property
    def title(self):
        return self.__title

    def to_dict(self):
        return {
            "type" : "Movie",
            "title"  : self.title,
            "creator" : self.creator,
            "release" : self.release
        }