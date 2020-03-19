import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

#checks for save.txt and gets information from file to initialize array from save file.
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        apps = tempApps.split(',')
        apps = [x for x in apps if x.strip()]


#allows you to add files to the array
def addFile():
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables",".exe"),("all files", "*.*")))
    if filename != "":
        apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

    print(apps)
    print("part 2")
    print(label)


#function to print files
def printFile():
    for app in apps:
        os.startfile(app, "print")

def clearFile():
    #clears apps array
    apps.clear()

    #clears list on screen
    for widget in frame.winfo_children():
        widget.destroy()


#creating GUI and elements inside
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#buttons
addFile = tk.Button(root, text="Select File", padx=10, pady=5, fg="white", bg="#263D42", command=addFile)
addFile.pack()

clearFile = tk.Button(root, text="Clear Files", padx=10, pady=5, fg="white", bg="#263D42", command=clearFile)
clearFile.pack()

printFile = tk.Button(root, text="Print Files", padx=10, pady=5, fg="white", bg="#263D42", command=printFile)
printFile.pack()

#initial place saved file array on screen
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()


with open('save.txt', "w") as f:
    for app in apps:
        f.write(app + ',')