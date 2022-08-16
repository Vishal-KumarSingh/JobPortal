import tkinter as tk
import tkinter.ttk as ttk
import networking
import variables
theme = "#FF6F61"
theme2="#FF7F70"
theme3="#FF7065"
text = "#ffffff"
def Profile():
    global pic
    profilerootm = tk.Toplevel()
    profileroot = tk.Frame(profilerootm , bg=theme )
    profilerootm.geometry("600x600")
    profilerootm.minsize("600", "600")
    profilerootm.maxsize("600","600")
    profilerootm.title("Profile")

    label = tk.Label(profileroot, text="Your Resume", font=(variables.font, 23, "bold"), bg=theme, fg=text)
    label.place(x=100, y=40, width="400", height="30")

    usernamelabel = tk.LabelFrame(profileroot, text="Username", bg=theme, fg=text, font=(variables.font, 13, "bold"))
    usernamelabel.place(x=20, y=120, width="270", height="50")
    userlabel = tk.Label(usernamelabel, text="id@example.com", bg=theme, fg=text, font=(variables.font, 13, "bold"))
    userlabel.place(x=10, y=5, width="200", height="20")
    tokenlabel = tk.LabelFrame(profileroot, text="Your Token", bg=theme, fg=text, font=(variables.font, 13, "bold"))
    tokenlabel.place(x=310, y=120, width="270", height="50")
    token = tk.Label(tokenlabel, text="XXXXXXXXXX", bg=theme, fg=text, font=(variables.font, 13, "bold"))
    token.place(x=10, y=5, width="200", height="20")

    rolelabel = tk.Label(profileroot, text="Role :- ", bg=theme, fg=text, font=(variables.font, 10, "bold"))
    rolelabel.place(x=30, y=200, width="200", height="30")
    roleText = tk.Entry(profileroot, fg=theme, font=(variables.font, 10, "bold"))
    roleText.place(x=310, y=200, width="200", height="30")

    experiencelabel = tk.Label(profileroot, text="Your Experience (in monthes)", bg=theme, fg=text, font=(variables.font, 10, "bold"))
    experiencelabel.place(x=30, y=250, width="200", height="30")
    expText = tk.Entry(profileroot, fg=theme, font=(variables.font, 10, "bold"))
    expText.place(x=310, y=250, width="200", height="30")

    edulabel = tk.Label(profileroot, text="Enter Your Education level", bg=theme, fg=text, font=(variables.font, 10, "bold"))
    edulabel.place(x=20, y=300, width="200", height="30")
    eduText = tk.Entry(profileroot ,fg=theme, font=(variables.font, 10, "bold"))
    eduText.place(x=310, y=300, width="200", height="30")



    skilllabel = tk.Label(profileroot, text="Enter Your Skills ", bg=theme, fg=text, font=(variables.font, 10, "bold"))
    skilllabel.place(x=20, y=350, width="200", height="30")
    skillText = tk.Text(profileroot ,fg=theme, font=(variables.font, 10, "bold"))
    skillText.place(x=310, y=350, width="200", height="100")



    def placedata(info):
        userlabel.config(text=info["username"])
        token.config(text=variables.loginToken)
        roleText.insert(tk.INSERT , info["role"])
        expText.insert(tk.INSERT ,info["experience"])
        eduText.insert(tk.INSERT ,info["education"])
        skillText.insert(tk.INSERT , info["skill"])

    def getdata():
        networking.Networking({"token": variables.loginToken}, "profile", command=placedata)
    def savedata():
        exp = expText.get()
        role=roleText.get()
        edu=eduText.get()
        skill = skillText.get("1.0", tk.END)
        networking.Networking({"token": variables.loginToken , "skills":skill,"experience":exp,"education":edu,"role":role}, "saveprofile", command=lambda e: print("saved"))

    pic = tk.PhotoImage(file=r"res\save.png")
    nextBtn = tk.Button(profileroot, image=pic, highlightthickness=0,bd=0, activebackground=theme, command=savedata)
    nextBtn.place(x=250, y=500, height="55", width="100")
    getdata()
    profileroot.place(x=0,y=0, width="600", height="600")
    profileroot.mainloop()
