import json
from json import JSONEncoder

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
        with(self.__user_json, "w") as memory:
            #json.dump(data, memory, cls=, indent=4)
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
