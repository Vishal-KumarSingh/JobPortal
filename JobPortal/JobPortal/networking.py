import json
from threading import Thread
import requests
class Networking():
    def __init__(self , jsondata , path , command):
        calller = Exec(jsondata,path,command)
        calller.start()

class Exec(Thread):
    def __init__(self, jsondata , path, command):
        super().__init__()
        self.url = "http://127.0.0.1:8000/" + path
        self.jsondata = jsondata
        print("Networking request log" + str(self.url) + str(jsondata))
        self.command = command
    def run(self):
        r = requests.post(self.url, json=self.jsondata)
        print("Networking response log" + r.text)
        self.command(r.json())
