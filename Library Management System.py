import tkinter as tk   
from tkinter import ttk  
import datetime   

window = tk.Tk()
window.title("Library Management System")
window.geometry("1000x500") 

label = tk.Label(window, text="Welcome to the Library Management System", font=("Arial", 14, "bold"))
label.pack(pady=20)

Sname = tk.StringVar()
Sroll = tk.IntVar()

tk.Label(window, text="Book Title:").pack()
name_entry = tk.Entry(window, textvariable=Sname, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(window, text="Book ID:").pack()
roll_entry = tk.Entry(window, textvariable=Sroll, font=("Arial", 12))
roll_entry.pack(pady=5)

books = {} 

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for book, info in books.items():
        tree.insert("", "end", values=(book, info.get("ID", ""), info.get("Status", ""), info.get("Date", "")))

def mark_borrowed():
    name = Sname.get()
    books[name] = {
        "ID": Sroll.get(),
        "Status": "Borrowed",
        "Date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    print("Borrowed", name)
    print(books)

    Sname.set("")
    Sroll.set("")
    refresh_table()

def mark_returned():
    name = Sname.get()
    books[name] = {
        "ID": Sroll.get(),
        "Status": "Returned",
        "Date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    print("Returned", name)
    print(books)

    Sname.set("")
    Sroll.set("")
    refresh_table()

def remove():
    name = Sname.get()
    del books[name]

    Sname.set("")
    Sroll.set("")
    refresh_table()

btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

borrow_btn = tk.Button(btn_frame, command=mark_borrowed, text="Borrow", bg="green", width=12)
return_btn = tk.Button(btn_frame, command=mark_returned, text="Return", bg="red", width=12)
remove_btn = tk.Button(btn_frame, command=remove, text="Remove", bg="blue",width=12)

borrow_btn.pack(side="left", padx=5)
return_btn.pack(side="left", padx=5)
remove_btn.pack(side="left", padx=5)

tree_frame = tk.Frame(window)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("Title", "ID", "Status", "Date")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)

tree.pack(side="left", fill="both", expand=True)

def on_tree_select(event):
    sel = tree.selection()
    if not sel:
        return
    item = sel[0]
    vals = tree.item(item, "values") 
    Sname.set(vals[0])
    try:
        Sroll.set(int(vals[1]))
    except (ValueError, TypeError):
        Sroll.set(0)

tree.bind("<<TreeviewSelect>>", on_tree_select)

refresh_table()


window.mainloop()
