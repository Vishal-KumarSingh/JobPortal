from threading import Thread
import json
import register
import variables
import dashboard
class GUImanager(Thread):

    def __init__(self):
        self.current_frame = None
        super().__init__()
        try:
            self.info = json.load(open("info/info.json"))
        except:
            string = '{"logintoken": "0" }'
            self.info = { "logintoken" : "0"}
            file = open("info/info.json",'w')
            file.write(string)
            file.close()

    def run(self):
        self.checkloginstatus()

    def checkloginstatus(self):
        if self.info["logintoken"] == "0":
            print("Login token not found redirecting to login frame")
            register.RegisterFrame()
        else:
            variables.loginToken=self.info["logintoken"]
            dashboard.dashboard()
            return 1

    def FramePlacer(self, frame , x=0 , y=0 , width=str(variables.size_x) , height=str(variables.size_y)):
        self.GUIcleaner()
        self.current_frame = frame
        frame.place(x=x, y=y , width=width , height=height)

    def GUIcleaner(self):
        if self.current_frame != None:
            self.current_frame.place_forget()
            print(" frame cleaned")
        pass