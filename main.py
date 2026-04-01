import openpyxl
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
employed = tk.BooleanVar()
path="people/people.xlsx"
comblist = ["Subscribed","Not Subscribed","Other"]
coldata = ("Name", "Age", "Subscription", "Employment")

def lighttheme():
    if theme.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

def load_data():
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    list_values = list(sheet.values)
    for colname in list_values[0]:
        treeview.heading(colname, text=colname)
    for data_values in list_values[1:]:
        treeview.insert('', tk.END, values=data_values)
    
def insert_data():
    name = name_entry.get()
    age = int(age_entry.get())
    subscription = combox.get()
    employment = "Employed" if employed.get() else "Unemployed"

    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    row_value = [name, age, subscription, employment]
    sheet.append(row_value)
    workbook.save(path)
    load_data()


style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
name_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5), pady=5)

age_entry = ttk.Spinbox(widgets_frame, from_=18, to=100)
age_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
age_entry.insert(0, "Age")
age_entry.bind("<FocusIn>", lambda e: age_entry.delete('0', 'end'))

combox = ttk.Combobox(widgets_frame, values=comblist)
combox.current(0)
combox.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

chkbox = ttk.Checkbutton(widgets_frame, text="Employed", variable=employed)
chkbox.grid(row=3,column=0, sticky="nsew", padx=5, pady=5)

inbton = ttk.Button(widgets_frame, text="Insert", command=insert_data)
inbton.grid(row=4, column=0, sticky="ewns", padx=5, pady=5)

saprater = ttk.Separator(widgets_frame)
saprater.grid(row=5, column=0, padx=(20, 20), pady=10, sticky="ew")

theme = ttk.Checkbutton(widgets_frame, text="Light Mode", style="Switch", command=lighttheme)
theme.grid(row=6, column=0, padx=5, pady=20, sticky="ewns")

treeframe = ttk.Frame(frame)
treeframe.grid(row=0, column=1, pady=10)

scroly = ttk.Scrollbar(treeframe)
scroly.pack(side="right", fill="y")

treeview = ttk.Treeview(treeframe, yscrollcommand=scroly.set, show="headings", columns=coldata, height=13)

treeview.column("Name", width=100)
treeview.column("Age", width=50)
treeview.column("Subscription", width=100)
treeview.column("Employment", width=100)

treeview.pack()

scroly.config(command=treeview.yview)

load_data()
root.mainloop()