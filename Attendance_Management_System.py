import tkinter as tk   #GUI library
from tkinter import ttk  #For Tableview
import datetime   #For date and time

window = tk.Tk()
window.title("Class Attendance")
window.geometry("1000x500") # Size of the Screenn

#GUI Element
label = tk.Label(window, text="Welcome to the Class Attendance System", font=("Arial", 14, "bold"))
label.pack(pady=20)


# Input Variables
Sname = tk.StringVar()
Sroll = tk.IntVar()

# GUI Name Input
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window, textvariable=Sname, font=("Arial", 12))
name_entry.pack(pady=5)

# GUI Roll Input
tk.Label(window, text="Roll:").pack()
roll_entry = tk.Entry(window, textvariable=Sroll, font=("Arial", 12))
roll_entry.pack(pady=5)


# Logic CRUD Operatons 

attendance = {} # dictionary to attendance records

#GUI Table Refresh Function
def refresh_table():
    # clear existing rows
    for row in tree.get_children():
        tree.delete(row)
    # insert current attendance dict
    for student, info in attendance.items():
        tree.insert("", "end", values=(student, info.get("Roll", ""), info.get("Status", ""), info.get("Date", "")))

# Mark Present Function
def mark_present():
    name = Sname.get()
    attendance[name] = {
        "Roll": Sroll.get(),
        "Status": "Present",
        "Date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    print("Present", name)
    print(attendance)
    # clear inputs
    Sname.set("")
    Sroll.set("")
    refresh_table()

# Mark Absent Function
def mark_absent():
    name = Sname.get()
    attendance[name] = {
        "Roll": Sroll.get(),
        "Status": "Absent",
        "Date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    print("Absent", name)
    print(attendance)
    # clear inputs
    Sname.set("")
    Sroll.set("")
    refresh_table()


# Delete Function
def delete():
    name = Sname.get()
    del attendance[name]
    # clear inputs
    Sname.set("")
    Sroll.set("")
    refresh_table()

     
# GUI Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

present_btn = tk.Button(btn_frame, command=mark_present, text="Present", bg="green", width=12)
absent_btn = tk.Button(btn_frame, command=mark_absent, text="Absent", bg="red", width=12)
delete_btn = tk.Button(btn_frame, command=delete, text="Delete", bg="blue",width=12)

present_btn.pack(side="left", padx=5)
absent_btn.pack(side="left", padx=5)
delete_btn.pack(side="left", padx=5)


# Attendance table 
tree_frame = tk.Frame(window)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("Name", "Roll", "Status", "Date")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)


tree.pack(side="left", fill="both", expand=True)

# Select row 
def on_tree_select(event):
    sel = tree.selection()
    if not sel:
        return
    item = sel[0]
    vals = tree.item(item, "values")  # (Name, Roll, Status, Date)
    Sname.set(vals[0])
    try:
        Sroll.set(int(vals[1]))
    except (ValueError, TypeError):
        Sroll.set(0)

tree.bind("<<TreeviewSelect>>", on_tree_select)



# Refresh table initially
refresh_table()


window.mainloop()