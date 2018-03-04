import requests

class Hue:
    storage=None

    def __init__(self,storage):
        self.storage = storage
    
    def sethost(self,host):
        self.storage["host"] = host
