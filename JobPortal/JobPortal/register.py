import tkinter as tk
import tkinter.ttk as ttk
import variables
import GUImanager
import json
import networking
import dashboard
def RegisterFrame():
     global pic
     theme = "#FF6F61"
     text = "#ffffff"
     Rgframe = tk.Frame(variables.root, bg= theme)
     label2 = tk.Label(Rgframe, text="Job Portal ", font=(variables.font, 45), bg=theme , fg=text)
     label2.place(x=50, y=130, width="400", height="100")

     desc = tk.Text(Rgframe ,  font=(variables.font+"ff", 13), bg=theme , fg=text,highlightthickness=0, bd=0)
     desc.insert("1.0", open("info/desc.txt").read())
     desc.place(x=100, y=230 , width="400", height="200")

     label = tk.Label(Rgframe , text="Sign Up", font = (variables.font , 25), bg=theme, fg=text)
     label.place(x=700 , y=130 , width="150" , height="40")

     emaillabel = tk.LabelFrame(Rgframe, text="   Enter your email", highlightthickness=0, bd=0,fg=theme,bg=text, font = (variables.font , 13, "bold"))
     emaillabel.place(x=700, y=200, width="300", height="50")
     emailText = tk.Entry(emaillabel, highlightthickness=0, bd=15,relief=tk.FLAT ,font = (variables.font , 13))
     emailText.place(x=0, y=0, width="280", height="30")

     passwordlabel = tk.LabelFrame(Rgframe, text="   Enter you password", highlightthickness=0, bd=0,fg=theme,bg=text, font = (variables.font , 13, "bold"))
     passwordlabel.place(x=700, y=300, width="300", height="50")
     passText = tk.Entry(passwordlabel, highlightthickness=0,bd=15,relief=tk.FLAT ,show="*", font = (variables.font , 13))
     passText.place(x=0, y=0, width="280", height="30")

     cnfpasswordlabel = tk.LabelFrame(Rgframe, text="   Enter you password again", highlightthickness=0, bd=0,fg=theme,bg=text, font = (variables.font , 13, "bold"))
     cnfpasswordlabel.place(x=700, y=400, width="300", height="50")
     cnfpassText = tk.Entry(cnfpasswordlabel, highlightthickness=0, bd=15,relief=tk.FLAT ,show="*", font = (variables.font , 13))
     cnfpassText.place(x=0, y=0, width="280", height="30")

     errlabel = tk.Label(Rgframe, foreground=text,  bg=theme ,font = (variables.font , 13))
     errlabel.place(x=700, y=450, width="400", height="30")
     def registration():
          email = emailText.get()
          pas = passText.get()
          cnfpass = cnfpassText.get()
          if pas != cnfpass:
              errlabel["text"] = "Password and confirm password must be same"
          else:
               networking.Networking({"email":email , "password" : pas} , "register" , command=saveToken)

     pic = tk.PhotoImage(file=r"res\signupbtn.png")
     registerbtn = tk.Button(Rgframe,activebackground=theme,image=pic,bd=0,bg=theme ,command=registration )
     registerbtn.place(x=770, y=500, width="150", height="55")

     lgnbtn = tk.Button(Rgframe, highlightthickness=0,font=("Helvetica", 12, "bold"),activebackground=theme, bd=0, bg=theme ,fg=text,text="Already have account ? Login here",command=LoginFrame)
     lgnbtn.place(x=700, y=580, width="300", height="30")

     variables.bgActivity.FramePlacer(Rgframe)

def LoginFrame():
     global pic
     theme = "#FF6F61"
     text = "#ffffff"
     Rgframe = tk.Frame(variables.root, bg=theme)
     label2 = tk.Label(Rgframe, text="Job Portal ", font=(variables.font, 45), bg=theme, fg=text)
     label2.place(x=50, y=130, width="400", height="100")

     desc = tk.Text(Rgframe, font=(variables.font + "ff", 15), bg=theme, fg=text, highlightthickness=0, bd=0)
     desc.insert("1.0", open("info/desc.txt").read())
     desc.place(x=100, y=230, width="400", height="200")

     label = tk.Label(Rgframe, text="Login", font=(variables.font, 25), bg=theme, fg=text)
     label.place(x=700, y=130, width="150", height="40")

     emaillabel = tk.LabelFrame(Rgframe, text="   Enter your email", highlightthickness=0, bd=0, fg=theme, bg=text,
                                font=(variables.font, 13, "bold"))
     emaillabel.place(x=700, y=200, width="300", height="50")
     emailText = tk.Entry(emaillabel, highlightthickness=0, bd=15, relief=tk.FLAT, font=(variables.font, 13))
     emailText.place(x=0, y=0, width="280", height="30")

     passwordlabel = tk.LabelFrame(Rgframe, text="   Enter you password", highlightthickness=0, bd=0, fg=theme, bg=text,
                                   font=(variables.font, 13, "bold"))
     passwordlabel.place(x=700, y=300, width="300", height="50")
     passText = tk.Entry(passwordlabel, highlightthickness=0, bd=15, relief=tk.FLAT, show="*",
                         font=(variables.font, 13))
     passText.place(x=0, y=0, width="280", height="30")


     def login():
          email = emailText.get()
          pas = passText.get()
          networking.Networking({"email": email, "password": pas}, "login", command=saveToken)

     pic = tk.PhotoImage(file=r"res\loginbtn.png")
     registerbtn = tk.Button(Rgframe, activebackground=theme, image=pic, bd=0, bg=theme, command=login)
     registerbtn.place(x=770, y=390, width="150", height="55")

     lgnbtn = tk.Button(Rgframe, highlightthickness=0, font=("Helvetica", 12, "bold"), activebackground=theme, bd=0,
                        bg=theme, fg=text, text="Already have account ? Login here", command=RegisterFrame)
     lgnbtn.place(x=700, y=450, width="300", height="30")

     variables.bgActivity.FramePlacer(Rgframe)

def saveToken(info):
     print(info["logintoken"])
     if info["logintoken"] != "0" and info["logintoken"] != "":
          string = '{"logintoken": "'+info["logintoken"]+'" }'
          file = open("info/info.json", 'w')
          file.write(string)
          file.close()
          variables.loginToken=info["logintoken"]
          dashboard.dashboard()

