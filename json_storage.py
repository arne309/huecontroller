import json

# this storage provider stores all data in a json file
# Take care, this is not safe for concurrent access!

class JsonStorage:

    data = None
    filename = ""
    
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename,"r") as f:
                self.data = json.load(f)

        except FileNotFoundError:
            self.data = dict()
        
    
    def safe(self):
        with open(self.filename,"w") as f:
            json.dump(self.data,f)

    
    def get(self,key):
        try:
            return self.data[key]
        except KeyError:
            return None
    
    def __getitem__(self,key):
        return self.get(key)
    
    def set(self,key,value):
        self.data[key] = value
        self.safe()
    
    def __setitem__(self,key,value):
        return self.set(key,value)
