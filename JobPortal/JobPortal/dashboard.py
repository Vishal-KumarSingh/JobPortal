import tkinter as tk
import tkinter.ttk as ttk
import variables
import GUImanager
import networking
import Profile
dashboardFrame = tk.Frame(variables.root, bg='white')
current_page = 0
Joblist = []
theme = "#FF6F61"
theme2="#FF7F70"
theme3="#FF7065"
text = "#ffffff"
Taglist=[]
pica = tk.PhotoImage(file=r"res\appliedbtn.png")
picb = tk.PhotoImage(file=r"res\applybtn.png")
def dashboard():
    headerFrame()
    profileFrame()
    navFrame()
    Sidebar()
    Page()
    bottombar()
    statusBar()
    variables.bgActivity.FramePlacer(dashboardFrame)
    print(variables.loginToken)
def headerFrame():
    headerFrame = tk.Frame(dashboardFrame)
    titlelabel = tk.Label(headerFrame, text="Job Portal", font=("Century Gothic" , 20), bg=theme , fg=text)
    titlelabel.place(x=0, y=0, width="400", height="45")
    sloganlabel = tk.Label(headerFrame, text="Your dream job is just a click away....", font=("Century Gothic", 10), bg=theme , fg=text)
    sloganlabel.place(x=0, y=45, width="400", height="25")
    headerFrame.place(x=0, y=0, height="70", width="400")

def profileFrame():
    global photo,pic
    profileframe = tk.Frame(dashboardFrame, bg=theme)

    pic = tk.PhotoImage(file=r"res\profile.png")
    probtn = tk.Button(profileframe, image=pic, highlightthickness=0, bd=0, command=Profile.Profile)
    probtn.place(x=725, y=0, width="30", height="30")
    photo = tk.PhotoImage(file=r"res\logout.png")
    lgbtn = tk.Button(profileframe, image = photo, highlightthickness = 0, bd = 0, command=logout)
    lgbtn.place(x=765, y=0, width="30", height="30")
    profileframe.place(x=400, y=0, height="30", width="800")

def navFrame():
    global photosearch

    navframe = tk.Frame(dashboardFrame, bg=theme)
    usernameabel = tk.Entry(navframe , )
    def click(*args):
        usernameabel.delete(0, 'end')
    usernameabel.insert(0, 'Search Jobs')
    usernameabel.pack(pady=10)
    usernameabel.bind("<Button-1>", click)
    usernameabel.place(x=560, y=5, width="200", height="30")


    photosearch = tk.PhotoImage(file=r"res\search.png")
    def search():
        global current_page
        text = usernameabel.get()
        current_page=0
        loadJob(0,text)
    lgbtn = tk.Button(navframe, image=photosearch ,highlightthickness = 0, bd = 0, command=search)
    lgbtn.place(x=765, y=5, width="30", height="30")
    navframe.place(x=400, y=30, height="40", width="800")

def Sidebar():
    global photosearch2,Taglist
    photosearch2 = tk.PhotoImage(file=r"res\search-b.png")
    sidebarframe = tk.Frame(dashboardFrame, bg=theme3)
    headinglabel = tk.Label(sidebarframe , text="Popular" , font=("Verdana" , 14 ),fg=text,bg=theme)
    headinglabel.place(x=0 , y=20 , height="50" , width="150")

    def placer(data):
        i=2
        def search(texts):
            global current_page
            current_page = 0
            loadJob(0, texts)
            print(texts)
        for tag in data:
            button = tk.Button(sidebarframe, text="   "+tag["title"]+"  ",bg=theme,fg=text, highlightthickness=0, bd=0, image=photosearch2,
                               compound=tk.LEFT , command=lambda text=tag["title"]: search(text))
            button.place(x=30, y=20 + i * 30, height="25")
            Taglist.append(button)
            i=i+1
    networking.Networking({"token":variables.loginToken}, "popularlist", command=placer)

    sidebarframe.place(x=0, y=72, height="580", width="250")


def Page():
    global pageframe
    pageframe = tk.Frame(dashboardFrame , bg="white")
    loadJob(0)
    pageframe.place(x=250, y=70 , width="950" , height="582")

def getJobFrame(pageframe, job):
    global pica,picb
    JobFrame = tk.Frame(pageframe,bg=theme2)
    recruiter = tk.Label(JobFrame , text = job["recruiter"], font=("Verdana" , 14 , "bold"), fg=text,bg=theme2)
    recruiter.place(x=10,y=10, height="25" , width="200")

    role = tk.Label(JobFrame, text=job["role"], fg=text,bg=theme2,font=("Verdana" , 12 , "bold"))
    role.place(x=0, y=60, height="20", width="300")

    salary = tk.Label(JobFrame, text=job["salary"],font=("Verdana" , 12 , "bold"),  fg=text,bg=theme2)
    salary.place(x=300, y=60, height="20", width="300")

    location = tk.Label(JobFrame, text=job["location"],font=("Verdana" , 12 , "bold"),  fg=text,bg=theme2)
    location.place(x=600, y=60, height="20", width="300")

    description = tk.Text(JobFrame , bg=theme2, font=("Helvetica", 11),bd=0, fg=text)
    description.insert(tk.INSERT , job["desc"])
    description.config(state=tk.DISABLED)
    description.place(x=10,y=90,height="80" , width="800")
    if job["applied"]:
        applybtn = tk.Button(JobFrame, image=pica, highlightthickness=0, bd=0, command=lambda: applyfor(job["id"]))
    else:
        applybtn = tk.Button(JobFrame, image=picb, highlightthickness=0, bd=0, command=lambda: applyfor(job["id"]))

    def applyfor(jobid):
        applybtn.configure(text="Applied")
        apply(jobid)
    applybtn.place(x=840 , y=140 , width="100", height="36")
    return JobFrame

def bottombar():
    global pic3 , pic4
    bottomBar = tk.Frame(dashboardFrame,bg=theme)
    pic3 = tk.PhotoImage(file=r"res\nextbtn.png")
    nextBtn = tk.Button(bottomBar,highlightthickness=0,bd=0,image=pic3, fg="white", activebackground=theme2, command=lambda : loadJob(current_page+3) )
    nextBtn.place(x=840, y=5, width="100", height="36")
    pic4 = tk.PhotoImage(file=r"res\previousbtn.png")
    PrevButton = tk.Button(bottomBar, image=pic4,  highlightthickness=0,bd=0,fg="white",activebackground=theme2, command=lambda : loadJob(current_page-3))
    PrevButton.place(x=100, y=5, width="100", height="36")

    bottomBar.place(x=250, y=654, width="950", height="48")

def statusBar():
    bottomBar = tk.Frame(dashboardFrame,bg=theme)
    status = tk.Label(bottomBar ,text=open("info/footer.txt").read(),fg=text,bg=theme)
    status.place( x=0 , y=20 , width="200", height="30")
    bottomBar.place(x=0, y=654, width="250", height="46")

def setJobs(data):
        global pageframe,current_page,Joblist
        current_page = data["offset"]
        removeJobs()
        Joblist = []
        i=0
        for jobs in data["joblist"]:
            # btn = tk.Button(pageframe,text="hhhhhh"+str(i)).pack()
            Job = getJobFrame(pageframe, jobs)
            Job.place(x=2, y=2 + i * 194, width="950", height="193")
            i=i+1
            Joblist.append(Job)
def removeJobs():
    global Joblist
    for job in Joblist:
        job.place_forget()
def loadJob(offset, searches=""):
    global current_page
    current_page=offset
    print("loading job")
    networking.Networking({"token": variables.loginToken, "offset": str(offset) , "search": searches}, "joblist", command=setJobs)
def apply(jobid):
    networking.Networking({"token": variables.loginToken, "jobid": str(jobid)}, "apply", command=lambda:print("applied"))
def logout():
    print("logout")
    variables.loginToken = "0"
    variables.bgActivity.info["logintoken"]=0
    string = '{"logintoken": "0" }'
    file = open("info/info.json", 'w')
    file.write(string)
    file.close()
    import register
    register.LoginFrame()

