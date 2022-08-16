import tkinter as tk
import tkinter.ttk as ttk

size_x = 1200
size_y = 700
root = tk.Tk()
design = ttk.Style()
font = "Century Gothic"
loginToken="0"
theme = "#FF6F61"
text = "#ffffff"
import GUImanager
bgActivity = GUImanager.GUImanager()
design.configure('warning.TButton', font=("Helvetica", 12, "bold"), foreground="white", background="red")
design.configure('submit.TButton', font=("Helvetica", 12, "bold"), foreground="black", background="blue")
design.configure('apply.TButton', font=("Helvetica", 8, "bold"), foreground="black", background="green")
