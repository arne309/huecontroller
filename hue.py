import requests, time, os, re

def printError(resp):
    print("Error: " + resp[0]["error"]["description"])

class Hue:
    storage=None

    def __init__(self,storage):
        self.storage = storage

        if not storage.get("hostname"):
            raise RuntimeError("No hostname configured!")
        
        if not storage.get("username"):
            self.auth()
    
    def sethost(self,host):
        self.storage["host"] = host
    
    def auth(self):
        url = "/api"

        success = False
        while not success:
            resp = self.rawpost(url,{"devicetype":"python_huecontroller#mba"})
            if "error" in resp[0].keys():
                printError(resp)
                time.sleep(1)
                
            elif "success" in resp[0].keys():
                self.storage.set("username",resp[0]["success"]["username"])
                print("Successfully authorized")
                success=True

    
    def getLights(self):
        return self.get("/lights")
    
    def getGroups(self):
        return self.get("/groups")

    def getRules(self):
        return self.get("/rules")
    
    # callback gets called with list of tuples: lightid, changed attribute, oldvalue, newvalue
    def watch(self, callback):
        lastState = self.getLights()

        while True:
            changes = list()
            time.sleep(2)

            currentState = self.getLights()

            for lightid,lightstate in currentState.items():
                for attribute, newvalue in lightstate.items():
                    oldvalue = lastState[lightid][attribute]
                    if oldvalue!=newvalue:
                        changes.append( (lightid,attribute,oldvalue,newvalue) )
            
            if len(changes)>0:
                callback(changes)
                lastState = currentState

    
    def get(self, url):
        assert(url[0]=="/")
        if not self.storage.get("username"):
            self.auth()

        r = requests.get("http://" + self.storage["hostname"] + "/api/" + self.storage.get("username") + url)
        assert(r.status_code==200)
        return r.json()

    def post(self, url, body):
        assert(url[0]=="/")
        if not self.storage.get("username"):
            self.auth()

        r = requests.post("http://" + self.storage["hostname"] + "/api/" + self.storage.get("username") + url, json=body)
        assert(r.status_code==200)
        return r.json()
    
    def rawpost(self, url, body):
        assert(url[0]=="/")
        r = requests.post("http://" + self.storage["hostname"] + url, json=body)
        assert(r.status_code==200)
        return r.json()
