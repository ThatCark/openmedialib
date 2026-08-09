import json
from json import JSONEncoder
from media import Media
from movie import Movie

class JSONConnector(MemoryConnector):
    def __init__(self, username):
        self.__user_json = username + ".json"
        self.__data = []

    def connect(self, db):
        with open(self.__user_json, "r") as memory:
            self.__data = memory.read()

    def close(self):
        self.__user_json = ""
        self.__data = []

    def save(self, *data):
        with open(self.__user_json, "w") as memory:
            json.dump(data, memory, cls=MediaEncoder, indent=4)
            #encoder required 
            #1. dump media
            #2. dump lending

    def load(self, user_id):
        if not self.__data.strip():
            return 
        
        #loaded_data = json_loads(self.__data, object_hook=)
        #object_hook required
    
        # except FileNotFoundError:
        #     return
        # except json.JSONDecodeError:
        #     return

    def media_hook(self, dct):
        if not (type in dct and creator in dct and release in dct):
            return
        if type == "Movie":
            return Movie(dct["creator"], dct["release"])

class MediaEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Media):
            return obj.to_dict()
        return super().default(obj)
